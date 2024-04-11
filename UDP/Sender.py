import socket
 
UDP_IP = "172.16.102.109"
UDP_PORT = 9327
MESSAGE = b"What's Up!"
 
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)) 