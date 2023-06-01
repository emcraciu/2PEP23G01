import tkinter as tk
import requests
import json
import multiprocessing

q = multiprocessing.Queue()
processes = []


class TimezoneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timezone App")
        self.timezone_listbox = tk.Listbox(self.root)
        self.timezone_listbox.pack(fill=tk.BOTH, expand=True)
        self.timezone_listbox.bind('<<ListboxSelect>>', self.display_time)
        self.load_timezones()

    def display_time(self, event):
        timezone = self.timezone_listbox.get(self.timezone_listbox.curselection())
        time_window = tk.Toplevel(self.root)
        time_window.title(f"Time in {timezone}")
        start_processes(timezone)
        time_label = tk.Label(time_window, text=q.get(timeout=5))
        time_label.pack()

    def load_timezones(self) -> list:
        response = requests.get(f'http://worldtimeapi.org/api/timezone*')

        if response.status_code == 200:
            timezones = response.json()
            for timezone in timezones:
                self.timezone_listbox.insert(tk.END, timezone)
            return timezones
        else:
            print("Error\n", "Failed to retrieve timezones.")


def time_zone(q: multiprocessing.Queue, region: str) -> None:
    response = requests.get(f'http://worldtimeapi.org/api/timezone//{region}')
    if response.status_code == 200:
        text = response.text
        time_zones = json.loads(text)
        my_time = time_zones["datetime"]
        q.put(my_time)


if __name__ == "__main__":
    def start_processes(reg) -> None:
        p = multiprocessing.Process(target=time_zone, args=(q, reg,))
        p.start()
        processes.append(p)
        for p in processes:
            p.join()


    root = tk.Tk()
    TimezoneApp(root)
    root.mainloop()
