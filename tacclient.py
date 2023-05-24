
import socket
import threading

HOST = "192.168.1.76"  # The server's hostname or IP address
PORT = 5000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def read_sok():
        while 1:
            data = s.recv(1024)
            print(data.decode('utf-8'))

    s.connect((HOST, PORT))
    potok = threading.Thread(target=read_sok)
    potok.start()
    while True:

        alias = input()
        s.sendall(alias.encode())
        #data = s.recv(1024)
        #print(f"Received {data!r}")

