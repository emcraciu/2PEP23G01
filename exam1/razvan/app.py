"""
Time difference app
"""
import tkinter as tk
import multiprocessing
import json
from datetime import datetime, timedelta
from tkinter import messagebox

import requests  # pylint: disable=import-error


def time_zone(city: str, que: multiprocessing.Queue):
    """receives time"""
    response = requests.get(f'http://worldtimeapi.org/api/timezone/Europe/{city}')
    text = response.text
    time_zones = json.loads(text)
    que.put(datetime.strptime(time_zones["utc_offset"].replace(':', ''), "%z"))


def time_diff(cities: list) -> timedelta:
    """in parallel, it calls on time_zone and then does the delta"""
    proc_list = []
    times = []
    que = multiprocessing.Queue()
    for city in cities:
        proc = multiprocessing.Process(target=time_zone, args=(city, que))
        proc.start()
        proc_list.append(proc)
    for proc in proc_list:
        proc.join()
    while not que.empty():
        times.append(que.get())
    if times[0] < times[1]:
        delta = times[1] - times[0]
    else:
        delta = times[0] - times[1]
    messagebox.showinfo("Sorted Data", delta)
    return delta


if __name__ == "__main__":
    root = tk.Tk()
    canvas1 = tk.Canvas(root, width=400, height=300)
    canvas1.pack()
    entry1 = tk.Entry(root)
    canvas1.create_window(200, 140, window=entry1)
    entry2 = tk.Entry(root)
    canvas1.create_window(200, 180, window=entry2)
    button1 = tk.Button(text='time delta', command=lambda: time_diff([entry1.get(), entry2.get()]))
    canvas1.create_window(200, 240, window=button1)
    root.mainloop()
