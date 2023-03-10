import re

my_string = '''my_text    is
1234
sfhasklgoiasdgasdh
mz_texx    is
5555
'''
my_string2 = '''me_text    sy
1324'''

# 2chr _ 4chr tab 2chr enter 4number

my_string2 == my_string

for index, letter in enumerate(my_string):
    # print(letter)
    if (index == 2 and letter != '_'):
        print("not the same")
    if (index in [7, 8, 9, 10] and letter != " "):
        print("not the same")
    if (index == 13 and letter != '\n'):
        print("not the same")

pattern = r'^\w{2}_\w{4}\s{4}\w{2}\n\d{4}'

result1 = re.findall(pattern, my_string)
result2 = re.findall(pattern, my_string2)
if result1 and result2:
    print('pattern is found in both texts')

pattern = r'(\w{2}_\w{4})\s{4}\w{2}\n\d{4}' # () this is a group
result3 = re.search(pattern, my_string)
print(type(result3))
print(result3.group(1))

