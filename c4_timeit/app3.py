""" Create a Context manager based on generators that will be able retrieve IP information and store it in context object"""

import os
import re
from contextlib import contextmanager


@contextmanager
def ip_information(os_type):
    if os_type == "nt":
        ip_command = "ipconfig"
    elif os_type == "posix":
        ip_command = "python3 --version"
    else:
        raise OSError

    obj = os.popen(ip_command)
    output = obj.read()
    pattern = r'\s+IPv4 Address(\.\s)+:\s*(?P<IPaddress>\d+\.\d+\.\d+\.\d+)'

    try:
        print('abcd')
        yield re.search(pattern, output).group('IPaddress')
    except Exception as e:
        print(e.args)
    finally:
        print("end")


if __name__ == '__main__':
    # print(ip_information("nt"))
    with ip_information("nt") as ip1:
        print(ip1)
        raise AttributeError("my_error")
        print(ip1)

#
# class My_File_Opener:
#
#     def __init__(self, file_name):
#         self.file = open(file_name, 'r')
#
#     def __enter__(self):
#         print('''in enter''')
#         return self
#
#     def __next__(self):
#         pass
#
#     def __iter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('''in exit''')
#
#
#
# # mfo = My_File_Opener('part1.py')
# # mfo.__enter__()
#
# with My_File_Opener('part1.py') as mfo:
#     print('running')
#     print(mfo)