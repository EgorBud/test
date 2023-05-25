import socket
import struct
from _thread import *
import json
import sqlite3 as sl
import asyncio

rooms=[[]]


#board = list(range(1,10))
async def draw_board(board, conn1, conn2):
    loop = asyncio.get_event_loop()
    s= ("-------------"+ '\n')
    for i in range(3) :
        s+= ("|"+ str(board[0+i*3])+ "|"+ str(board[1+i*3])+ "|"+ str(board[2+i*3])+ "|"+ '\n')
        s+= ("-------------"+'\n')
    await loop.sock_sendall(conn1, str.encode(s))
    await loop.sock_sendall(conn2, str.encode(s))
async def take_input(player_token, conn, board):
    loop = asyncio.get_event_loop()
    valid = False
    while not valid:
        player_answer = (await loop.sock_recv(conn, 1024)).decode('utf8')#("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
             await loop.sock_sendall(conn, str.encode(("Некорректный ввод. Вы уверены, что ввели число?")))
             continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = (player_token)
                valid = True
            else:
                 await loop.sock_sendall(conn, str.encode( ("Эта клеточка уже занята")))
        else:
             await loop.sock_sendall(conn, str.encode( ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")))
async def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
async def tic( conn1, conn2, board = list(range(1,10))):
    counter = 0
    win = False
    while not win:
        await draw_board(board, conn1, conn2)
        if counter % 2 == 0:
            await  take_input("X", conn1, board)
        else:
            await take_input("O", conn2, board)
        counter += 1
        if counter > 4:
            tmp = await check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    await draw_board(board, conn1, conn2)

async def btn_click(comp_choise, choise):

    if choise == comp_choise:
        print("Ничья")
        return 0
    elif choise == '1' and comp_choise == '2' \
            or choise == '2' and comp_choise == '3' \
            or choise == '3' and comp_choise == '1':
        print("Победа 1")
        return 1
    else:
        print("Проигрыш 1")
        return -1

async def tictactoe(conn1, conn2):
    await tic(conn1, conn2)

async def rpc(conn1, conn2):
    loop = asyncio.get_event_loop()
    ch1 = (await loop.sock_recv(conn1, 1024)).decode('utf8')
    ch2 = (await loop.sock_recv(conn2, 1024)).decode('utf8')
    res =  await btn_click(ch1, ch2)
    await loop.sock_sendall(conn1, str.encode((str(res))))
    await loop.sock_sendall(conn2, str.encode(str(-res)))

async def client_handler(connection, connection2):
    loop = asyncio.get_event_loop()
    print(connection)
    data = (await loop.sock_recv(connection, 1024)).decode('utf8')
    message = json.loads(data)
    #message = data
    print(message['task'])
    try:
        func = globals()[message['task']]
        await func(connection, connection2)
    except Exception as e:
        print(e)
        await loop.sock_sendall(connection, str.encode('error'))
    await loop.sock_sendall(connection, str.encode('end'))
    connection.close()
    connection2.close()



async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.1.76', 1233))
    server.listen()
    server.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, _ = await loop.sock_accept(server)
        ((await loop.sock_recv(client, 1024)).decode('utf8'))

        client2, _ = await loop.sock_accept(server)
        loop.create_task(client_handler(client, client2))

asyncio.run(run_server())