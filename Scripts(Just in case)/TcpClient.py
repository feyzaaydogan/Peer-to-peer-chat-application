import socket
import sys
import time
import json
import string
import datetime
import os

print(" Hello! Please enter your file path as it is explained in the README.TXT")
filePath=str(input())


while 1:
    cik = True
    ipAddr = ""
    file = open(os.path.join(filePath, "Output.txt"), "r")
    if file.mode == "r":
        contents = file.read()
        print(contents)

    else:
        print("Error")

    Buddy=input("Who do you want to chat?")
    Buddy=str(Buddy)
    if contents.find(Buddy)!=-1:
        start = contents.find(Buddy)+len(Buddy)+4
        while(contents[start]!="'"):
           ipAddr=ipAddr+contents[start]
           start=start+1


    else:
        print("Kisi listede degil")
        cik=False


    while cik:
        try:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         port = 5001
         s.connect((ipAddr, port))

         message=input("Please Enter your messages--If you want to leave write quit")

         if(message=="quit"):
            cik=False
            text_file = open(os.path.join(filePath, "ChatLog.txt"), "w")
            text_file.write("")
            text_file2 = open(os.path.join(filePath, "ChatLogNoDelete.txt"), "a")
            text_file2.write("************NEW LOG**************\n")
            text_file2.close()
            text_file.close()
            break

         else:
            message = str(message + "--" + str(datetime.datetime.now()))
            s.send(message.encode())
            s.close()
            text_file = open(os.path.join(filePath, "ChatLog.txt"), "a")
            text_file.write("Ben:"+message+"--->MessageSent\n")
            text_file2=open(os.path.join(filePath, "ChatLogNoDelete.txt"),"a")
            text_file2.write("Ben:"+message+"--->MessageSent\n")
            text_file2.close()
            text_file.close()
            time.sleep(1)


        except:
            print("Connection can not be established")
            cik=True
            break