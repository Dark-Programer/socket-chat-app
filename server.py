import threading
import socket

ip_address = '127.0.0.1'
port_address = 55555

socket_type = socket.AF_INET
protocol_name = socket.SOCK_STREAM

# making a server
server = socket.socket(socket_type, protocol_name)
server.bind((ip_address, port_address))
server.listen()

clients = []
nicknames = []


def broadcast(msg):
    for client in clients:
        client.send(msg)


# when a client produces some error this 'handle()' function remove that clint from the list
def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat...".encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # client send a msg to the server to get his nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nick name of the client is: {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send("connected to the server!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


print("Server is on...")
receive()
