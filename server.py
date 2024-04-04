import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',))


ip_add = input("ip address:")


if ip_add == "":
    ip_add = "172.16.102.102"
    
    
    
LISTENING_PORT = 8640

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',))
    s.bind(('', LISTENING_PORT))
    s.listen(3)

    print ("server is running")
    
    while True:
        
        socket_connection, address = s.accept()
        
        connections.append(socket_connection)
        
        threading.Thread(target=handle_user_connection, args = [socket_connection, address]).start()
except Exception as e:
    print(f"An error has occured")