from socket import *
import os

print(" Hello! Please enter your file path as it is explained in the README.TXT")
filePath=str(input())

text_file = open(os.path.join(filePath, "ChatLog.txt"), "w")
text_file.write("")
text_file.close()

print("----Chat----")


def GetYourName(addresss):
   thisIp = ""
   addresss=str(addresss)
   i=2
   while addresss[i]!="'":
      thisIp=thisIp+addresss[i]
      i=i+1

   file = open(os.path.join(filePath, "Output.txt"), "r")
   isim = ""
   if file.mode == "r":
      dosya = file.read()
      index = dosya.find(thisIp) - 5
      while dosya[index] != "'":
         isim = isim + dosya[index]
         index = index - 1
   isim = isim[::-1]
   file.close()
   return isim


while 1:
   print("******")
   serverPort = 5001
   host = ""
   serverSocket = socket(AF_INET, SOCK_STREAM)
   serverSocket.bind((host, serverPort))
   serverSocket.listen(1)
   connectionSocket, addr =serverSocket.accept()
   message=connectionSocket.recv(4096)
   message=message.decode()
   message=str(GetYourName(addr))+":"+message
   text_file = open(os.path.join(filePath, "ChatLog.txt"), "a")
   text_file.write(str(message)+" -->MessageRecieved"+"\n")
   text_file=open(os.path.join(filePath, "ChatLog.txt"),"r")
   print(text_file.read())
   text_file.close()

   text_file2 = open(os.path.join(filePath, "ChatLogNoDelete.txt"), "a")
   text_file2.write(str(message)+" -->MessageRecieved"+"\n")
   text_file2.close()

   serverSocket.close()