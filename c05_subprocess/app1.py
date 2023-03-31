"""
* get IP address from OS
"""
import os
import re
import sys
import time
import subprocess
from subprocess import CalledProcessError


class Utils:

    def get_ip_adress(self):
        result = subprocess.Popen(['ipconfig'], text=True, stdout=subprocess.PIPE)
        output = result.communicate()[0]
        matches = re.finditer(r'(Ethernet|Wireless)(\s\w+)+', output)
        interfaces = []
        for match in matches:
            interfaces.append(match.group())
        ip_matches = re.finditer(r"disconnected|(?<=(Address. . . . . . . . . . . : ))(\d+\.)+\d+", output)
        ip_addresses = []
        for ip_match in ip_matches:
            ip_addresses.append(ip_match.group())
        dict = {interfaces[i]: ip_addresses[i] for i in range(len(interfaces))}
        return dict

    def connect_ssh(self, ip: str):
        with subprocess.Popen(['ssh', '-T', f'exevil1@{ip}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as ssh:
            time.sleep(3)
            stdout, stderr = ssh.communicate(input=b'Yes')
            print(stdout)
            print(stderr)
            ssh.terminate()

    def allow_user_to_enter_message(self):
        notepad = subprocess.Popen(['notepad.exe', 'file.txt'], stdin=subprocess.PIPE)
        stdout, stderr = notepad.communicate(input=b'Yes')
        notepad.terminate()

    def fail_a_program(self, exit_code):
        failed_program = subprocess.run([sys.executable, '-c',  f'exit({exit_code})'])
        try:
            failed_program.check_returncode()
        except CalledProcessError:
            print(f'Application has failed with return code: {failed_program.returncode}')

    def ping(self, ip_address):
        ping_var = subprocess.Popen(['ping', ip_address], stderr=subprocess.PIPE)
        try:
            stdout, stderr = ping_var.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            ping_var.send_signal(9)
            stdout, stderr = ping_var.communicate()
        print(stderr)

    def search_for_erors(self, level='ERROR', path=''):
        if os.path.isfile(path):
            cat = subprocess.Popen(['cat', path], stdout=subprocess.PIPE)
            grep = subprocess.Popen(['grep', level], stdin=cat.stdout, stdout=subprocess.PIPE)
            cat.stdout.close()
            output = grep.communicate()[0]

        if os.path.isdir(path):
            output = subprocess.run(['dir'], shell=True, text=True, capture_output=True, cwd=path)
            files = output.stdout
            output2 = re.search(files, r"\d+\/\d+\/\d+\s+\d+:\d+\s\w+\s+(\d+,?){0,5}\s(?P<file>.*)")
            print(output2)
            cat = subprocess.Popen(['cat', '/var/log/wifi.log'], stdout=subprocess.PIPE)
            grep = subprocess.Popen(['grep', level], stdin=cat.stdout, stdout=subprocess.PIPE)
            cat.stdout.close()
            output = grep.communicate()[0]
            print(output)

utils = Utils()
# print(utils.get_ip_adress())
utils.fail_a_program(10)
# utils.connect_ssh('192.168.1.31')
#utils.allow_user_to_enter_message()