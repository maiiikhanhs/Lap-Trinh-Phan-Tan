import socket
import random

HOST = "192.168.1.135"
PORT = 6349
N = 10

A = [random.randint(1, 100) for _ in range(N)]
message = ' '.join(map(str, A))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode())
    result = s.recv(1024).decode()
    print("Result from server:", result)
