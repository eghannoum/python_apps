
from pyexpat.errors import messages
import socket
import threading
import queue

from grpc import server


msgs = queue.Queue()
clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 0000))


def receive():
    while True:
        try:
            msg, addr = server.recvfrom(1024)
            msgs.put(msg, addr)
        except:
            pass


def broadcast():
    while True:
        while not msgs.empty():
            try:
                msg, addr = messages.get()
                print(msg.decode())
                if addr not in clients:
                    clients.append(addr)
                for client in clients:
                    if msg.decode().startwith('SIGNUP_TAG:'):
                        name = msg.decode()[msg.decode().index(':')+1:]
                        server.sendto(f'{name} joined!'.encode(), client)
                    else:
                        server.sendto(msg, client)
            except:
                clients.remove(client)


thread_1 = threading.Thread(target=receive)
thread_2 = threading.Thread(target=broadcast)

thread_1.start()
thread_2.start()
