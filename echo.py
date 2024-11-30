import socket

s = socket.socket()

s.connect(("ad.samsclass.info", 10203))

print(s.recv(1024).decode())
s.send("Goodbye\n".encode())
print(s.recv(1024).decode())
s.close()
