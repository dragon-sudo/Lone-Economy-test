#!/bin/bash

# 检查参数是否正确
if [ $# -ne 3 ]; then
  echo "Usage: $0 search_string input_file output_file"
  exit 1
fi

# 获取输入参数
search_string=$1
input_file=$2
output_file=$3

# 搜索指定内容，并将结果保存到新的文件中
grep -n "$search_string" "$input_file" > "$output_file"

# 输出结果到控制台
cat "$output_file"
