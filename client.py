import socket
import threading

ip_address = '127.0.0.1'
port_address = 55555

socket_type = socket.AF_INET
protocol_name = socket.SOCK_STREAM

# taking input from user
nickname = input("Enter your nickname: ")

# making a server
client = socket.socket(socket_type, protocol_name)
client.connect((ip_address, port_address))


def receive():
    while True:
        try:
            msg = client.recv(20480).decode('ascii')
            if msg == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(msg)

        except:
            print("Error occurred!")
            client.close()
            break


def write():
    while True:
        msg = (f'{nickname}: {input("")}')
        client.send(msg.encode('ascii'))


receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()
