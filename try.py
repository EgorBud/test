drow=0
lose=0
win=0
def btn_click(comp_choise, choise):

    if choise == comp_choise:
        print("Ничья")
        return 0
    elif choise == 1 and comp_choise == 2 \
            or choise == 2 and comp_choise == 3 \
            or choise == 3 and comp_choise == 1:
        print("Победа")
        return 1
    else:
        print("Проигрыш")
        return -1

btn_click(3, 2)






board = list(range(1,10))
def draw_board(board):
    print ("-------------")
    for i in range(3) :
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = (player_token)
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)
main(board)










import json
import socket
import threading

HOST = "192.168.1.76"  # The server's hostname or IP address
PORT = 1233  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    def read_sok():
        while 1:
            data = s.recv(1024)
            mes=data.decode()
           # mes=json.load(data)
            if(mes==('end')):
                s.close()
                break
            if (data is None):
                s.close()
                break
            print(mes)

    s.connect((HOST, PORT))
    potok = threading.Thread(target=read_sok)
    potok.start()
    while True:

        alias = input()
        try:
            s.sendall(json.dump(alias))
        except:
            break
        #data = s.recv(1024)
        #print(f"Received {data!r}")