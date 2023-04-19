import random
import socket
import time
from threading import Thread


def is_prime(number: int):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def primes(limit: int):
    time.sleep(random.randint(1, 3))
    result = []
    for i in range(1, limit + 1):
        if is_prime(i):
            result.append(i)
    print(result)
    return result


class Connect:

    def __init__(self, host: str, port: int):
        self.sock = socket.socket()
        self.host = host
        self.port = port

class Client(Connect):
    def start(self) -> None:
        self.thd1 = Thread(target=primes, args=(200,))
        self.thd1.start()


class Server(Connect):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.sock.bind((self.host, self.port))

    def start(self):
        self.sock.listen(1)
        self.thd1 = Thread(target=self.recv_msg)
        self.thd1.start()

    def recv_msg(self):
        print('BEFORE RECEIVE')
        #conn, addr = self.sock.accept()


server = Server('localhost', 1502)
client = Client('localhost', 1501)
server.start()
client.start()

