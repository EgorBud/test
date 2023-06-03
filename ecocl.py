import threading
import json
import socket

HOST = '127.0.0.1'
PORT = 3003
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def read():
        while 1:
            data = json.loads(s.recv(1024).decode('utf8'))
            print(data)
            if (data["task"] == ('chat')):
                print(data["show"])
            if (data["task"] == ("game")):
                print("change board and let next move")
                print(data["move"])
            if (data["task"] == ("end")):
                print("result:")
                print(data["result"])
                break
            if not data:
                break
    s.connect((HOST, PORT))
    data = s.recv(1024).decode('utf8')
    i=0
    while(i!=1):
        login="man"
        password="123"
        #login=input()
        #password=input()
        m = {"task": "load", "log": login, "pas": password}
        data = json.dumps(m)
        s.sendall((bytes(data, encoding="utf-8")))
        data = json.loads(s.recv(1024).decode('utf8'))
        i=data["state"]
        if(i!=1):
            print(i)
    user = data["user"]
    print(user)
    #g=input()
    g='t'
    if(g=="t"):
        #key=input()
        key="any"
        m = {"task": "ticroom", "key":key}
        data = json.dumps(m)
        s.sendall((bytes(data, encoding="utf-8")))
        data = json.loads(s.recv(1024).decode('utf8'))
        print(data)
        if(data['task']=="wait"):
            print("wait")
        data = json.loads(s.recv(1024).decode('utf8'))
        print(data)
        potok = threading.Thread(target=read)
        print(22)
        potok.start()

        while(potok.is_alive()):
            g=input()
            if(g != '1'):
                mes=g
                m = {"task": "chat", "show": mes}
                data = json.dumps(m)
                s.sendall((bytes(data, encoding="utf-8")))
            else:
                print("turn")
                t=input()
                m = {"task": "game", "choise": t}
                data = json.dumps(m)
                s.sendall((bytes(data, encoding="utf-8")))
    if (g == "r"):
        # key=input()
        key = "any"
        m = {"task": "rpcroom", "key": key}
        data = json.dumps(m)
        s.sendall((bytes(data, encoding="utf-8")))
        data = json.loads(s.recv(1024).decode('utf8'))
        print(data)
        if (data['task'] == "wait"):
            print("wait")
        data = json.loads(s.recv(1024).decode('utf8'))
        print(data)
        potok = threading.Thread(target=read)
        print(22)
        potok.start()

        while (potok.is_alive()):
            g = input()
            if (g != '1'):
                mes = g
                m = {"task": "chat", "show": mes}
                data = json.dumps(m)
                s.sendall((bytes(data, encoding="utf-8")))
            else:
                print("turn")
                t = input()
                m = {"task": "game", "choise": t}
                data = json.dumps(m)
                s.sendall((bytes(data, encoding="utf-8")))


    s.close()






'''
import json
import socket

HOST = '127.0.0.1'
PORT = 3003
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    i=0
    data = s.recv(1024).decode('utf8')

    m = {"task": "ticroom", "log": "man", "pas": "123", "key": 'key'}
    data = json.dumps(m)
    s.sendall((bytes(data, encoding="utf-8")))

    while(1):
        data = s.recv(1024).decode('utf8')
        print(data)
        if not data:
            s.close()
            break
        try:
            message = json.loads(data)
            print(message['show'])
            if(message['task']=='get'):
                alias = input()
                if(alias in '123456789'):
                    m = {"task": "game","choise":alias, "log": "man", "pas": "123", "key":'key'}
                else:
                    m = {"task": "chat", "show": alias, "log": "man", "pas": "123", "key": 'key'}
                data = json.dumps(m)
                s.sendall((bytes(data, encoding="utf-8")))
            if (message['task']== ('wait')):
                data1=message
                while(data1['task']!='stop'):
                    data1 = json.loads(s.recv(1024).decode('utf8'))
                    print(data1)
                continue
            if (message['task']== ('end')):
                s.close()
                break
        except Exception as e:
            print(e)
        if (i==1):
            i = 2
            continue





'''







'''




    def read_sok():
        while 1:
            data = s.recv(1024)
            if(data.decode('utf-8')==('end')):
                s.close()
                print('s')
                break
            if not data:
                s.close()
                break
            print(data.decode('utf-8'))

    s.connect((HOST, PORT))
    potok = threading.Thread(target=read_sok)
    potok.start()
    i=0
    alias = input()


    m = {"task": alias, "log": "man", "pas": "123"}
    data = json.dumps(m)
    s.sendall((bytes(data,encoding="utf-8")))
    #data = s.recv(1024)
    #print(f"Received {data!r}")
    while i != 1:

        alias = input()

        m = {"task": alias, "log": "man", "pas": "123"}
        data = json.dumps(m)
        try:
            s.sendall((bytes(data, encoding="utf-8")))
        except:
            break
        # data = s.recv(1024)
        # print(f"Received {data!r}")




'''


'''import socket

HOST = "192.168.1.76"  # The server's hostname or IP address
PORT = 1234  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    alias = input()
    s.sendall(alias.encode())
    alias = input()
    s.sendall(alias.encode())
    alias = input()
    s.sendall(alias.encode())
    data = s.recv(1024)
    print(f"Received {data!r}")

'''