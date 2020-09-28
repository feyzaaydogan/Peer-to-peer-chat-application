from socket import *
import sys
import time
import json

# Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


i=0
index=0
addresX=gethostbyname(gethostname())
addresXNew=""
while(index<len(addresX)):
    if(addresX[index]=="."):
        i=i+1

    addresXNew=addresXNew+addresX[index]
    if i==3:
        break
    index=index+1
addresXNew=addresXNew+"255"
print(addresXNew)


server_address = (addresXNew, 5000)

response = input("Adinizi giriniz")
response = str(response)
json_data = {
            "username":response,
            "ip_address":gethostbyname(gethostname())

}
dict=json.dumps(json_data)
while True:
        print('responding...')
        sent = sock.sendto(str(dict).encode(), server_address)
        time.sleep(60)