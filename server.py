import socket
import select
server=socket.socket()
serverport=12345
server.bind(('',serverport))
server.listen(5)

clients = []

while True: 
    empfangen, senden_unbenutzt, notrufe_unbenutzt  = select.select([server] + clients, [], [])

    for sock in empfangen: 
        if sock is server: 
            client, addr = server.accept() 
            clients.append(client) 
            print("+++ Ein Socket zwischen Client",addr[0],"mit Client-Port",addr[1],
                  "und diesem Server mit Server-Port",serverport,"wurde hergestellt.")
        else: 
            nachricht = sock.recv(1024) 
            ip = sock.getpeername()[0]
            port = sock.getpeername()[1]
            if nachricht: 
                print("[",ip,':',port,"]",nachricht.decode('utf-8')) 
            else: 
                print("--- Verbindung zu",ip," wurde beendet") 
                sock.close() 
                clients.remove(sock) 