#!/usr/bin/bash
set -euo pipefail
linux_output_dir="${1:?请由 study.sh 提供实验目录}"
linux_student='Linux 学习者'
linux_values=(2 5 8 11)
linux_total=0
for linux_value in "${linux_values[@]}"; do
    if (( linux_value >= 6 )); then
        linux_total=$((linux_total + linux_value))
    fi
done
printf '你好，%s\n选中数字的和：%s\n' "$linux_student" "$linux_total"
[[ "$linux_total" == 19 ]]
printf 'total=%s\n' "$linux_total" > "$linux_output_dir/result.txt"
