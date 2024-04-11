import socket

ADDR = ('172.28.1.109', 9327)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(ADDR)

while True:
    data, addr = s.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")