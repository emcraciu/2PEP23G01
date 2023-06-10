"""Exam Python M2
Create Python UI application that will compare 2 time zones:

2 fields will be created where user can specify zone
1 button that will print the difference between the timezones when pressed
Points:
read user input - 20p
retrieve time data from https://worldtimeapi.org/api/timezone/Europe/ in parallel - 20p
calculate time difference and print - 20p
documentation and type hints - 20p
one unittest and pylint score of 10 - 20p"""


import tkinter as tk
import asyncio
import aiohttp
import json

async def regions(session, region):
    # Uncomment the following lines to make an actual API request
    # response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe/{region}')
    # text = await response.text()
    # time_zone = json.loads(text)

    # For demonstration purposes, use the provided sample data
    text = '{"abbreviation":"CEST","client_ip":"92.82.223.58","datetime":"2023-06-10T16:03:35.918111+02:00","day_of_week":6,"day_of_year":161,"dst":true,"dst_from":"2023-03-26T01:00:00+00:00","dst_offset":3600,"dst_until":"2023-10-29T01:00:00+00:00","raw_offset":3600,"timezone":"Europe/Budapest","unixtime":1686405815,"utc_datetime":"2023-06-10T14:03:35.918111+00:00","utc_offset":"+02:00","week_number":23}'
    time_zone = json.loads(text)
    return int(time_zone["datetime"].split('+')[1][:2])

async def compare_timezone():
    async with aiohttp.ClientSession() as session:
        available_regions = await regions(session, "utc")


        # for region in available_regions:
        #     result_text.insert(tk.END, f"- {region}\n")

async def main():
    window = tk.Tk()
    window.title("Comparison of 2 time zones")

    label1 = tk.Label(window, text="Timezone 1:")
    label1.pack()
    entry1 = tk.Entry(window)
    entry1.pack()

    label2 = tk.Label(window, text="Timezone 2:")
    label2.pack()
    entry2 = tk.Entry(window)
    entry2.pack()

    compare_button = tk.Button(window, text="Compare", command=lambda: asyncio.create_task(compare_timezone()))
    compare_button.pack()

    result_text = tk.Text(window, width=60, height=20)
    result_text.pack()

    window.mainloop()

if __name__ == "__main__":
    asyncio.run(main())


