import socket

#making a socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Connecting to the server with url and port using socket
mysocket.connect(('data.pr4e.org',80))
#making a get request to the resource on the server.encoding make unicode characters to utf-8
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#sending the get request to the server
mysocket.send(cmd)


while True:
    data=mysocket.recv(512)
    if len(data)<1:
        break
    print(data.decode())

#closing the socket once data is retreived
mysocket.close()