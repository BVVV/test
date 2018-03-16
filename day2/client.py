import socket

client = socket.socket()
client.connect(("localhost", 6969))
client.send("你好".encode())
data = client.recv(1024)
print(data.decode())
client.close()
