import socket
import sys
import json
from datetime import time
import os

def PrintOnline(list):

    for x in list:
        print(x,list[x], "is Online")
    print("****0****\n\n")



print(" Hello! Please enter your file path as it is explained in the README.TXT")
filePath=str(input())




sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('', 5000)

sock.bind(server_address)

list={}
dogru=False

limit=0

while True:
    try:
       if limit<=50:

        print('waiting to receive')
        data, server = sock.recvfrom(4096)
        parsed_json = json.loads(data)
        server=str(server)
        i=2
        rcvIP=str("")
        while server[i]!="'":
           rcvIP=rcvIP+server[i]
           i=i+1

        if(parsed_json["username"]) in list:
            print("Already in the list")
        else:
            list[parsed_json['username']] = rcvIP
            text_file = open(os.path.join(filePath, "Output.txt"),"w")
            text_file.write(str(list))
            text_file.close()
            limit = limit + 1

        PrintOnline(list)

       else:
           print("Capacity is full!")
           break

    except:
        print("Error")

