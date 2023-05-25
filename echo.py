# echo-server.py

import socket

HOST = "192.168.1.76"  # Standard loopback interface address (localhost)
PORT = 1234  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            print(1)
            data = conn.recv(1024).decode()
            print(data)
            if not data:
                break
            conn.sendall(data.encode())