import socket, threading

connections = []

def handle_user_connection(connection: socket.socket, address: str) -> None:
    '''
        Get user connection in order to keep receiving their messages and
        sent to others users/connections.
    '''
    while True:
        try:
            # Get client message
            msg = connection.recv(1024)

            # If no message is received, there is a chance that connection has ended
            # so in this case, we need to close connection and remove it from connections list.
            if msg:
                # Log message sent by user
                print(f'{address[0]}:{address[1]} - {msg.decode()}')
                
                # Build message format and broadcast to users connected on server
                msg_to_send = f'From {address[0]}:{address[1]} - {msg.decode()}'
                # broadcast(msg_to_send, connection)

            # Close connection if no message was sent
            else:
                # remove_connection(connection)
                break

        except Exception as e:
            print(f'Error to handle user connection: {e}')
            # remove_connection(connection)
            break


HOST = '172.28.3.26'
PORT = 8640
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(3)
    print('server started')
    while True:

            # Accept client connection
            socket_connection = s.accept()[0]
            # Add client connection to connections list
            connections.append(socket_connection)
            # Start a new thread to handle client connection and receive it's messages
            # in order to send to others connections
            threading.Thread(target=handle_user_connection, args=[socket_connection, "172.28.0.241"]).start()

