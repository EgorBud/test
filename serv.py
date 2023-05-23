import socket
import sqlite3 as sl
con = sl.connect('my-test.sql')
with con:
    data = con.execute("SELECT * FROM USER ")
    for row in data:
        print(row)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('192.168.1.76',5000))
client = [] # Массив где храним адреса клиентов
print ('Start Server')
while 1 :
         data , addres = sock.recvfrom(1024)
         print (addres)
         if  addres not in client :
                 client.append(addres)# Если такого клиента нету , то добавить
         for clients in client :
                 if clients == addres :
                     continue # Не отправлять данные клиенту, который их прислал
                 sock.sendto(data,clients)