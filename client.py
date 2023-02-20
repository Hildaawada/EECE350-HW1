from time import time
import uuid
import socket
from datetime import datetime
start_time=time()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverPort =4359
host_name=(socket.gethostbyname(socket.gethostname()))
s.connect((host_name,serverPort))
websiteIP = input('Enter desired IP address:')
s.send(websiteIP.encode())
#print a message with the request details and the exact time sent
print("message sent at:", datetime.utcnow())
print("request is:", websiteIP)
modifiedSentence = s.recv(4096)
# message received at time
print ('From Server:')
print(modifiedSentence)
print("exact time of response:", datetime.utcnow())
print ("The MAC address in formatted way is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
s.close()
end_time=time()
totalroundtriptime=end_time-start_time
# total round trip time, we get the time after w close all sockets and the response received
print("total round trip time", totalroundtriptime)
