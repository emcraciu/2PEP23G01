import os
import re


class SystemInformation:
    @staticmethod
    def ip_getter():
        result = os.popen('ipconfig')
        for line in result.readlines():
            pattern = r"IPv4 Address.*: (?P<IP>.*)"
            match = re.search(pattern, line)
            if match:
                print(match.group("IP"))

    @staticmethod
    def cp_usage():
        result = os.popen('wmic cpu get loadpercentage')
        for line in result.readlines():
            pattern = r"(?P<cpu_usage>\d+)"
            match = re.search(pattern, line)
            if match:
                print(match.group("cpu_usage"))


SystemInformation.ip_getter()
SystemInformation.cp_usage()