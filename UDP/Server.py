import socket

udp_ip = '172.28.1.120'
udp_port = 9327

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((udp_ip, udp_port))

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print("recieved message: %s" % data)
    else:
        continue