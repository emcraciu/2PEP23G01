from time import sleep
from queue import Queue
import requests
from threading import Thread
import random
from multiprocessing import Process
from multiprocessing import Queue as Queue_Proc


def get_numbers(length: int, queue: Queue) -> None:
    nr_list = []
    response = requests.get(
        f'https://www.random.org/integers/?num={length}&min=33&max=126&col=1&base=10&format=plain&rnd=new')
    text = response.text
    for number in text.strip().split("\n"):
        nr_list.append(int(number))
    queue.put(random.choice(nr_list))


def get_pass_threads(nr_char: int) -> str:
    my_q = Queue()
    threads = []
    for i in range(nr_char):
        thd1 = Thread(target=get_numbers, args=(10, my_q))
        thd1.start()
        threads.append(thd1)
    for i in threads:
        i.join()
    password = ""
    for _ in threads:
        password += chr(my_q.get())
    return password


def get_pass_multiprocessing(nr_char: int) -> str:
    my_q_m = Queue_Proc()
    processes = []
    for i in range(nr_char):
        process = Process(target=get_numbers, args=(10, my_q_m,))
        process.start()
        processes.append(process)
    for p in processes:
        p.join()
    password = ""
    for _ in processes:
        password += chr(my_q_m.get())
    return password







if __name__ == "__main__":
    # print(f'Your password is: \"{get_pass_threads(int(input("Password length: ")))}\"\n'
    #       f'Keep it safe! We won\'t')
    print(f'Your password is: \"{get_pass_multiprocessing(int(input("Password length: ")))}\"\n'
          f'Keep it safe! We won\'t')


