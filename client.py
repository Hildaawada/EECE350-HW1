from time import time
import uuid
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverPort =4359
s.connect(("192.168.0.106",serverPort))
websiteIP = input('Enter desired IP address:')
s.send(websiteIP.encode())
modifiedSentence = s.recv(4096)
#print a message with the request details and the exact time sent
print("request received"," at exact time:",time())
print ('From Server:')
print(modifiedSentence.decode())
print("exact time of response:", time())
print ("The MAC address in formatted way is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
s.close()
# total round trip time, we get the time after w close all sockets and the response received
print("total round trip time", time())
