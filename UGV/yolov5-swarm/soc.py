import socket

HOST = '192.168.31.91'  # 替换为您的目标IP地址
PORT = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    # string_to_send = "action1"  # 替换为您要发送的字符串
    string_to_send = input()
    s.sendall(string_to_send.encode())
    data = s.recv(1024)
    print('Received', repr(data))
    # s.shutdown(socket.SHUT_WR)  # 关闭套接字的输出流
    # s.close()