import subprocess, shlex

command = "python ttime.py"
p = subprocess.Popen(shlex.split(command), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# 为子进程传递参数
p.stdin.write('5\n')
# 实时获取输出
while p.poll() == None:
    out = p.stdout.readline().strip()
    if out:
        print("sub process output: ", out)
# 子进程返回值
print("return code: ", p.returncode)
