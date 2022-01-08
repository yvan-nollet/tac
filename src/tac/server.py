import socket
from _thread import *
import typing as t


def read_pos(s: str) -> t.Tuple[int, int]:
    s = s.split(",")
    return int(s[0]), int(s[1])

def make_pos(tup: t.Tuple[int, int]) -> str:
    return str(tup[0]) + "," + str(tup[1])


server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started, waiting for a connection")

# positions of our players
pos = [
    (0, 0),
    (100, 100),
]

def threaded_client(conn, player: int):
    conn.send(str.encode(make_pos(pos[player])))
    reply = pos
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print(f"Received: {data}")
                print(f"Sending: {reply}")

            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1