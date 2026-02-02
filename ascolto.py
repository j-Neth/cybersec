import socket
server_socket = socket.socket()
host = '127.0.0.1'
port = 6364
server_socket.bind((host, port))
server_socket.listen(1)
f = open("logfile.txt", "w")
f.write(f"Listening on {host}:{port}... \n")
for i in range(6):
    conn, addr = server_socket.accept()
    f.write(f"Connection from {addr} \n")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            richiesta = data.decode()
            if richiesta == 'SHUTDOWN':
                break
            risposta = f"Received: {richiesta}"
            conn.sendall(risposta.encode())
        if richiesta == 'SHUTDOWN':
            break
    finally:
        conn.close()
f.close()
server_socket.close()