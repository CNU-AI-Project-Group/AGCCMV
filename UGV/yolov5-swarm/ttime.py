# coding:utf-8
# file: called.py
import time, sys
try:
    # 获取标准输入
    N = int(sys.stdin.readline())
except ValueError:
    # 标准错误信息
    sys.stdout.write("numeric input required!!\n")
    sys.stdout.flush()
    exit(1)
else:
    for i in range(N):
        # 标准输出
        sys.stdout.write("%d\n" %i)
        sys.stdout.flush()
        time.sleep(1)
    exit(0)