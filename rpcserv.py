import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('192.168.1.76',5000))
client = [] # Массив где храним адреса клиентов
print ('Start Server')
while 1 :
         conn , addres = sock.recvfrom(1024)
         print (addres)
         with conn:
             print(f"Connected by {addres}")
             while True:
                 data = conn.recv(1024)
                 if not data:
                     break
                 conn.sendall(data)
         if  addres not in client :
                 client.append(addres)# Если такого клиента нету , то добавить
         for clients in client :
                 if clients == addres :
                     continue # Не отправлять данные клиенту, который их прислал
                 sock.sendto(data,clients)