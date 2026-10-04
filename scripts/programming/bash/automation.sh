#!/usr/bin/bash
set -euo pipefail
linux_output_dir="${1:?请由 study.sh 提供实验目录}"
mkdir -p -- "$linux_output_dir/input"
printf '第一行\n第二行\n' > "$linux_output_dir/input/课程 笔记.txt"
printf '第三行\n' > "$linux_output_dir/input/another.txt"
linux_total=0
while IFS= read -r -d '' linux_file; do
    linux_lines=$(wc -l < "$linux_file")
    linux_total=$((linux_total + linux_lines))
    printf '%s\t%s\n' "$linux_lines" "${linux_file##*/}"
done < <(find "$linux_output_dir/input" -type f -name '*.txt' -print0)
[[ "$linux_total" == 3 ]]
printf 'total_lines=%s\n' "$linux_total" > "$linux_output_dir/result.txt"
printf '总行数：%s\n' "$linux_total"
