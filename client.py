import socket
import threading
import random

from scipy import rand

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind('localhost', random.randint(1000, 9000))
name = input('Nickname: ')


def receive():
    while True:
        try:
            msg, _ = client.recvfrom(1024)
            print(msg.decode())
        except:
            pass


thread = threading.Thread(target=receive)
thread.start()

client.sendto(f'SIGNUP_TAG: {name}'.encode(), ('localhost', 0000))


while True:
    msg = input('')
    if msg == '!q':
        exit()
    else:
        client.sendto(f'{name}: {msg}'.encode(), ('localhost', 0000))
