import socket
host = '192.168.1.76'
port = 1233

ClientSocket = socket.socket()
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(2048)
while True:
    Input = input('Your message: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))
    if Input == 'BYE':
        break
    if Response.decode('utf-8') == 'BYE':
        break
ClientSocket.close()