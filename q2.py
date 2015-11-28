import socket
import sys

ip = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
get_request = 'GET / HTTP/1.1\r\n\r\n'
user_agent = 'User-Agent: Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) ' \
             'Presto/2.9.201 Version/12.02\r\n\r\n'
s.send(get_request + user_agent)
s.close()
