import subprocess

# 下面一行是将要执行的另外的线程
print('call() test:', subprocess.call(['python', 'protest.py']))
print('')
# 调用 check_call()函数执行另外的线程，配送码是 0
print('check_call() test:', subprocess.check_call(['python', 'protest.py']))
print('')
# 调用 getstatusoutput()函数执行另外的线程
print('getstatusoutput() test:', subprocess.getstatusoutput(['python', 'protest.py']))
print('')
# 调用 getoutput()函数执行另外的线程
print('getoutput() test:', subprocess.getoutput(['python', 'protest.py']))
print('')
# 调用 check_output()函数执行另外的线程，输出二进制结果
print('check_output() test:', subprocess.check_output(['python', 'protest.py']))
