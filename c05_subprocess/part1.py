import subprocess
import time

result = subprocess.Popen(['ipconfig'], text=True, stdout=subprocess.PIPE)
output = result.communicate()[0]
print(output)
print(80*'#')

# subprocess.run(["cmd"])
print(80*'#')
subprocess.run(["dirx"], shell=True)
print(80*'#')
# subprocess.run(["notepad"])
print(80*'#')
subprocess.run(["route", "print", "-6"])
print(80*'#')

# ssh = subprocess.Popen(['ssh', '-T', '192.168.1.31'], shell=True)
# stdout, stderr = ssh.communicate(input=b'ls')
# print(stdout, stderr)

notepad = subprocess.Popen(['notepad.exe', 'file.txt'])
time.sleep(10)
stdout, stderr = notepad.communicate(input=b'yes')
notepad.terminate()