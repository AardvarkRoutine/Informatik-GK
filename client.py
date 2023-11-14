import socket
client=socket.socket()
serverip='127.0.0.1'
serverport=12345
client.connect((serverip,serverport))
client.send(bytes('hhhhgggg','utf-8'))
client.close()