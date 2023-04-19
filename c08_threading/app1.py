import time
from threading import Thread


def is_prime(number: int):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def primes(limit: int):
    result = []
    for i in range(1, limit + 1):
        if is_prime(i):
            result.append(i)
    return result


class Client(Thread):
    def run(self) -> None:
        try:
            output = primes(200)
        finally:
            del self._target, self._args, self._kwargs
        return output


class Server(Thread):
    def run(self) -> None:
        try:
            primes(200)
        finally:
            del self._target, self._args, self._kwargs


client = Client()
server = Server()
print(client.start())
print(server.start())
print(server.join())
print(client.join())

