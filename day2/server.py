import socket

server = socket.socket()

server.bind(("localhost", 6969))
server.listen()
conn, address = server.accept()
data = conn.recv(1024)
print(data.decode())
conn.send("你是谁？".encode())
conn.close()

