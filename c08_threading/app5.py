import socket
import random
import time
from threading import Thread

MESSAGE = 'DONE'

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
    return result


class AlreadySetError(Exception):
    pass


class Connect:

    def __init__(self, host: str, port: int):
        self.sock = socket.socket()
        self.host = host
        self.port = port

    def generate_prime(self):
        primes_list = list(filter(lambda no: True if no > 129 else False, primes(256)))
        self.prime = random.choice(primes_list)

    def get_prime(self, prime):
        if not getattr(self, "prime", False):
            self.prime = prime
            print(f'received prime: {self.prime}')
        else:
            raise AlreadySetError('Value for prime already set to:', self.prime)

    def generate_base(self):
        if getattr(self, "prime", False):
            self.base = random.randint(2, self.prime - 1)
        else:
            raise AttributeError('Value for prime needs to be set first')

    def get_base(self, base):
        if not getattr(self, "base", False):
            self.base = base
            print(f'received base: {self.base}')
        else:
            raise AlreadySetError('Value for base already set to:', self, base)

    def generate_local_secret(self):
        self.__local_secret = random.randint(2, self.prime)
        x = pow(self.base, self.__local_secret) % self.prime
        print(self.__class__.__name__, x)
        return x

    def get_secret(self, secret):
        self.__shared_secret = pow(secret, self.__local_secret) % self.prime + 129
        print(self.__class__.__name__, "Shared secret: ", self.__shared_secret)

    def send_encrypted_message(self, message):
        # my code 

class Client(Connect):
    def start(self) -> None:
        self.thd1 = Thread(target=self.send_msg)
        self.thd1.start()

    def send_msg(self):
        self.sock.connect((self.host, self.port))
        self.generate_prime()
        self.generate_base()

        self.sock.send(bytes(f'{self.prime}', encoding='UTF-8'))
        self.sock.send(bytes(f'{self.base}', encoding='UTF-8'))
        time.sleep(0.2)
        remote_secret = self.generate_local_secret()
        self.sock.send(bytes(f'{remote_secret}', encoding='UTF-8'))
        self.get_secret(int(self.sock.recv(4096)))


class Server(Connect):
    def __init__(self, host, port):
        super().__init__(host, port)
        self.sock.bind((self.host, self.port))

    def start(self):
        self.sock.listen(1)
        self.thd1 = Thread(target=self.recv_msg)
        self.thd1.start()

    def recv_msg(self):
        conn, addr = self.sock.accept()
        self.get_prime(int(conn.recv(4096)))
        self.get_base(int(conn.recv(4096)))
        time.sleep(0.1)
        remote_secret = self.generate_local_secret()
        self.get_secret(int(conn.recv(4096)))
        conn.send(bytes(f'{remote_secret}', encoding='UTF-8'))


server = Server('localhost', 1502)
client = Client('localhost', 1502)
server.start()
client.start()


server.thd1.join()
client.thd1.join()
