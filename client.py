#V1, written by Preston, who's clueless as to what any of this means but is trying his best. Pretty much copied from geeksforgeeks.

#imports socket library
import socket

#creates socket object
s = socket.socket()

#Port that will be refernced for connecting to server
port = 0000

#Connects to server with given arguments
s.connect(('insert ip here', port))

#Receives something from the server, I don't know what :)
print(s.recv(1024).decode())

#closes the connection, becuase we're gentlemen and don't leave the door open
s.close