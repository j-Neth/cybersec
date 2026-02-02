import socket
s = socket.socket()
s.settimeout(2)
indirizzo = '127.0.0.1'
porta = 6364
s.connect((indirizzo, porta))
s.sendall(b'Hello World!V')
risposta = s.recv(1024)
print(risposta.decode())
s.close()