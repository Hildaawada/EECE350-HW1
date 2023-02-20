from time import time
from datetime import datetime
import requests
import socket
#proxy server
SPS = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket successfully created")
serverPORT=4359
proxyIP=(socket.gethostbyname(socket.gethostname())) #this is the local server's IP address
print(proxyIP)
SPS.bind((proxyIP,serverPORT))
SPS.listen(1)
print ("The server is ready to receive")

while True:
    try:
        c, addr = SPS.accept()
        INPUT= c.recv(4096)
        print("message received from", addr)
        INPUT = INPUT.decode()
        print("Request received",INPUT)
        #a 3rd socket might help in directly sending the request to the destination address, it only communicates with the client
        #it is used to avoid this confusion when the proxy server wants to send
        PSW=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        PSW.connect((INPUT,80))
        request_string=f"GET / HTTP/1.1\r\nHost:{INPUT}\r\n\r\n"
        # send the client's request to the destination server
        print("request to destination server:",request_string)
        print("request to destination server at exact time",datetime.utcnow())
        PSW.send(request_string.encode())
        response_string=PSW.recv(4096)
        # print a message that the response was recieved with the exact time
        print("response received"," at exact time:",datetime.utcnow())
        PSW.close()
        #print a message that the response was sent with the exact time
        c.send(response_string)
        print("response sent"," at exact time:", datetime.utcnow())
        c.close()
        
    except Exception as error:
        print("error:", error)

