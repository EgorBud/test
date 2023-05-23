import socket

HOST = "192.168.1.76"  # The server's hostname or IP address
PORT = 5000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    alias = input()
    s.sendall(alias.encode())
    data = s.recv(1024)

print(f"Received {data!r}")