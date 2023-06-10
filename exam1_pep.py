"""Instant time zone calculator"""

from multiprocessing import Process, Queue
import json

import tkinter

import requests

q = Queue()


def get_time(city: str) -> None:
    """Get time data for specified city"""
    response = requests.get(f'http://worldtimeapi.org/api/timezone/Europe/{city}', timeout=10)
    text = response.text
    time_text = json.loads(text)
    q.put((city, time_text['utc_offset']))
    response.close()


def calculate_difference(data1: str, data2: str) -> str:
    """calculate difference relative to UTC hour offset string"""
    return str(int(data1[1:3]) - int(data2[1:3]))


if __name__ == '__main__':

    def print_difference() -> None:
        """get time for 2 cities and calculate time difference"""
        for city in city1.get(), city2.get():
            proc = Process(target=get_time(city))
            proc.start()
        city_1, offset1 = q.get()
        city_2, offset2 = q.get()
        print(f'Difference between {city_1} and {city_2} is: '
              f'{calculate_difference(offset1, offset2)}h')


    main_window = tkinter.Tk()
    city1 = tkinter.Entry(main_window)
    city1.pack()
    city2 = tkinter.Entry(main_window)
    city2.pack()
    get_button = tkinter.Button(main_window, text='TZ difference', command=print_difference)
    get_button.pack()
    main_window.mainloop()
