"""Create Python UI application that will compare 2 time zones:

    2 fields will be created where user can specify zone
    1 button that will print the difference between the timezones when pressed
    Points:
    read user input - 20p
    retrieve time data from https://worldtimeapi.org/api/timezone/Europe/ in parallel - 20p
    calculate time difference and print - 20p
    documentation and type hints - 20p
    one unittest and pylint score of 10 - 20p
"""

import json
import tkinter
import requests
import pylint


provided_city = input("please insert the city desire from Europe: ")
provided_city2 = input("please provide the second Europe City: ")

main_window = tkinter.Tk()
main_window.title('City Zone')
city_one = tkinter.Label(main_window, text=provided_city)
city_one.grid(row=0, column=0, sticky=tkinter.E)
city_two = tkinter.Label(main_window, text=provided_city2)
city_two.grid(row=1, column=0, sticky=tkinter.E)
button2 = tkinter.Button(main_window, text="Time_dif", command=provided_city)
button2.grid(row=2, column=0)
main_window.mainloop()


def get_city():
    """function description"""
    response = requests.get('https://worldtimeapi.org/api/timezone/Europe/' + provided_city, timeout=1)
    text = response.text
    city_info = json.loads(text)
    first_date = city_info['datetime']
    #first_date(key=lambda x:datetime.strptime(time1,"%Y-%m-%d %H:%M:%S"))
    return first_date


def get_city2():
    """function description"""
    response2 = requests.get('https://worldtimeapi.org/api/timezone/Europe/' + provided_city2, timeout=1)
    text = response2.text
    city_info2 = json.loads(text)
    second_date = city_info2['datetime']
    #second_date(key=lambda x:datetime.strptime(time2,"%Y-%m-%d %H:%M:%S"))
    return second_date

time1 = get_city()
time2 = get_city2()
#print(time1-time2)

options = ["--disable=unnecessary-lambda,missing-function-docstring", 'examen.py']
pylint.run_pylint(argv=options)
