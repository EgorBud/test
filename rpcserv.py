import socket
def btn_click(comp_choise, choise):

    if choise == comp_choise:
        print("Ничья")
        return 0
    elif choise == 1 and comp_choise == 2 \
            or choise == 2 and comp_choise == 3 \
            or choise == 3 and comp_choise == 1:
        print("Победа 1")
        return 1
    else:
        print("Проигрыш 1")
        return -1


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind (('192.168.1.76',5000))
print ('Start Server')
sock.listen()
conn1, addres1 = sock.accept()
conn2, addres2 = sock.accept()
ch1=conn1.recv(1024)
ch2=conn2.recv(1024)