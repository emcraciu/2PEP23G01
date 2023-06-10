'''Create Python UI application that will:
* retrieve timezones from this link: (50p)
  * http://worldtimeapi.org/api/timezone*
  * Allow the user to select a timezone and open a new window indicating the time in the selected timezone using this link: (50p)
  * http://worldtimeapi.org/api/timezone/<area>/<zone>
Detailed description:
  - all windows must have title (5p)
  - all modules classes and methods must be documented (10p)
  - type hints should be used whenever possible (5p)
  - at least two unittests created for at lest one function (20p)
  - all timezones are displayed. (30p)
  - each timezone clicked will open a new window and show time in that timezone (20p)
  - retrieving time to display is done async or in separate thread or process (10p)

Note: You can choose to pack new Frame or open new window for each displayed time.
For new window you can use tkinter.TopLevel(main_window)'''

import tkinter as tk
import requests
import threading
from tkinter import ttk
import tkinter


class Timezone:

    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Timezone App")

        # Create a text box to display  timezones
        self.n = tk.StringVar()
        self.timezone_text = ttk.Combobox(self.main_window, width = 27, textvariable = self.n)
        self.timezone_text.pack()

        #  button for display time
        self.display_button = tk.Button(self.main_window, text="Display Time", command=self.new_window)
        self.display_button.pack()

        #  timezones
        self.timezones = []
        self.retrieve_timezones()

    def retrieve_timezones(self):
           response = requests.get("http://worldtimeapi.org/api/timezone")
           #text = response.text
           self.timezones = response.json()
           # Adding combobox drop down list
           self.timezone_text['values'] = self.timezones


    def retrieve_time(self, timezone):
        #how to retrieve time from timezone
        response = requests.get(f"http://worldtimeapi.org/api/timezone/{timezone}")
        data = response.json()
        current_time = data['datetime']
        return current_time


        #self.time_label.config(text=current_time)


    def new_window(self):
        # Create a new window to display time
        window = tkinter.Tk()
        new_title = self.n.get()
        window.title(new_title)
        # Create a text to display the time
        responce = tkinter.Text(window)
        responce.pack()

        # Create a label to display the time (you may try and this)
        # time_label = tk.Label(window)
        # time_label.pack()

        # insert timezone in a text area
        current_time = self.retrieve_time(new_title)
        responce.insert('1.0', current_time)



    # you can try and this method. Atention have to change on  self.display_button with self.display_time
    # def display_time(self):
        # timezone = self.timezone_text.get()
        #
        # # Create a new window to display time
        # time_newwindow = tk.Toplevel(self.main_window)
        # time_newwindow.title(timezone)
        #
        # # Create a label to display the time
        # self.time_label = tk.Label(time_newwindow)
        # self.time_label.pack()
        #
        # # How to find running time of a thread in Python
        # threading.Thread(target=self.retrieve_time, args=(timezone,)).start()

    # def retrieve_time(self, timezone):
    #     #how to retrieve time from timezone
    #     response = requests.get(f"http://worldtimeapi.org/api/timezone/{timezone}")
    #     data = response.json()
    #     current_time = data['datetime']
    #     self.time_label.config(text=current_time).





if __name__ == '__main__':
    main_window = tk.Tk()
    app = Timezone(main_window)
    main_window.mainloop()