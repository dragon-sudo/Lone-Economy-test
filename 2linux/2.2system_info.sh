#!/bin/bash

# 显示硬盘使用情况
echo "Hard Disk Usage:"
df -h

# 显示内存使用情况
echo "Memory Usage:"
free -h

# 显示 CPU 使用情况
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'
