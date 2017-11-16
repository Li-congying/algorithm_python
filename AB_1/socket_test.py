import socket

host = 'www.weibo.com'
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
buffer = []
while True:
    s.send('GET / HTTP/1.1\r\nHost: www.weibo.com\r\nConnection: close\r\n\r\n')
    d = s.recv(1024)
    print d
    buffer.append(d)