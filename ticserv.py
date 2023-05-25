import socket


board = list(range(1,10))
def draw_board(board, conn1, conn2):
    s= ("-------------"+ '\n')
    for i in range(3) :
        s+= ("|"+ str(board[0+i*3])+ "|"+ str(board[1+i*3])+ "|"+ str(board[2+i*3])+ "|"+ '\n')
        s+= ("-------------"+'\n')
    conn2.sendall(str.encode(s))
    conn1.sendall(str.encode(s))
def take_input(player_token, conn):
    valid = False
    while not valid:
        player_answer = conn.recv(1024).decode()#("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            conn.sendall(str.encode(("Некорректный ввод. Вы уверены, что ввели число?")))
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = (player_token)
                valid = True
            else:
                conn.sendall(str.encode( ("Эта клеточка уже занята")))
        else:
            conn.sendall(str.encode( ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")))
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
def main(board, conn1, conn2):
    counter = 0
    win = False
    while not win:
        draw_board(board, conn1, conn2)
        if counter % 2 == 0:
            take_input("X", conn1)
        else:
            take_input("O", conn2)
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
    draw_board(board, conn1, conn2)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind (('192.168.1.76',1234))
client = [] # Массив где храним адреса клиентов
print ('Start Server')


sock.listen()
conn1, addres1 = sock.accept()
conn2, addres2 = sock.accept()
main(board, conn1, conn2)
conn1.sendall(str.encode('end'))
conn2.sendall(str.encode('end'))
conn2.close()
conn1.close()