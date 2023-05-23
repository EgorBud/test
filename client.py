import socket
import threading
def read_sok():
    while 1 :
        data = sor.recv(1024)
        print(data.decode('utf-8'))
server = ('127.0.0.4', 5000)# Данные сервера
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.connect(server)
alias = input() # Вводим наш псевдоним



#sor.bind(('127.0.0.10', 0)) # Задаем сокет как клиент

sor.sendall(alias.encode())# Уведомляем сервер о подключении
print('s')
potok = threading.Thread(target= read_sok)

potok.start()
while 1 :
    mensahe = input()
    sor.sendall(mensahe.encode())#