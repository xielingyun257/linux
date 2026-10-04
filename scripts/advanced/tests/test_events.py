"""测试真正的数据边界和 CLI 退出契约，输出仅用仓库内临时目录。"""
import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

DIRECTORY = Path(__file__).resolve().parents[1]
ROOT = DIRECTORY.parents[1]
sys.path.insert(0, str(DIRECTORY))
from event_model import Event
from log_cli import summarize


class EventTests(unittest.TestCase):
    def setUp(self):
        self.row = {'timestamp':'2026-10-05T09:00:00', 'level':'ERROR',
                    'component':'camera', 'duration_ms':'12.5'}

    def test_numeric_conversion(self):
        self.assertEqual(Event.from_row(self.row).duration_ms, 12.5)

    def test_reject_bad_values(self):
        for change in ({'duration_ms':'nan'}, {'duration_ms':'inf'}, {'duration_ms':'-1'},
                       {'level':'OTHER'}, {'component':''}, {'timestamp':'yesterday'}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                Event.from_row({**self.row, **change})

    def test_missing_field(self):
        self.row.pop('duration_ms')
        with self.assertRaises(ValueError):
            Event.from_row(self.row)


class CliTests(unittest.TestCase):
    def setUp(self):
        parent = ROOT/'scripts/runtime/test-temp'
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent)
        self.directory = Path(self.temporary.name)
        self.input = self.directory/'input.csv'
        self.input.write_text('timestamp,level,component,duration_ms\n2026-10-05T09:00:00,ERROR,camera,20\nBROKEN,ROW\n')

    def tearDown(self):
        self.temporary.cleanup()

    def invoke(self, *extra):
        return subprocess.run(['/usr/bin/python3','-E','-s',str(DIRECTORY/'log_cli.py'),
                               '--input',str(self.input),'--output',str(self.directory/'report.json'),*extra],
                              capture_output=True, text=True)

    def test_summary_excludes_invalid_from_denominator(self):
        report = summarize(self.input)
        self.assertEqual(report['valid_records'], 1)
        self.assertEqual(report['error_rate'], 1.0)
        self.assertEqual(len(report['invalid_records']), 1)

    def test_strict_status_and_report(self):
        result = self.invoke('--strict')
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertTrue((self.directory/'report.json').exists())

    def test_threshold_status(self):
        self.assertEqual(self.invoke('--max-error-rate','0.5').returncode, 4)

    def test_preserve_existing_output(self):
        output = self.directory/'report.json'
        output.write_text('original')
        self.assertEqual(self.invoke().returncode, 2)
        self.assertEqual(output.read_text(), 'original')

    def test_empty_is_not_zero(self):
        self.input.write_text('timestamp,level,component,duration_ms\n')
        self.assertIsNone(summarize(self.input)['error_rate'])

    def test_empty_cli_is_inconclusive(self):
        self.input.write_text('timestamp,level,component,duration_ms\n')
        self.assertEqual(self.invoke().returncode, 5)

    def test_bad_header(self):
        self.input.write_text('wrong,header\n')
        self.assertEqual(self.invoke().returncode, 2)


if __name__ == '__main__':
    unittest.main()
