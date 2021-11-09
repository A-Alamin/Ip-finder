print('''
        ggggggg  gg  ggggggg  gg        gggggggg  gggggggg
        gg       gg  gg    g  gg        gg        gg    gg
        gg       gg  ggggggg  gggggggg  ggggggg   gggggggg
        gg       gg  gg       gg    gg  gg        gg gg
        ggggggg  gg  gg       gg    gg  gggggggg  gg   gg


[--]                 Ip-Finder 127.0.0.1                        [--]
[--]            Created by: Alamin Ahmed (Cipher)               [--]
                        Version: 1.1.0                  
[--]            Follow us on Twitter: @Cipherbyte               [--]
[--]            Follow us on kooapps: @Cipherbyte               [--]
[--]            Follow us on Facebook:@Cipherbyte               [--]

Ip-Finder is a product of Cipherbyte, Follow us on social media for more security demo and awareness.
For update visit https://github.com/m-3r ''')
print('.')
print('.')
import time
import socket
import sys,threading,os,platform
put = input("Enter Website Domin Name: ")
IP = socket.gethostbyname(put)
print('.')
time.sleep(1)
print('Looking for site ip address...')
time.sleep(3)
print('.')
print(put,'Ip Address Is',IP)
time.sleep(1)
print("\nRuning autoscan on",put)
time.sleep(1)
print(".")
print("Scanning Ip for open ports...")
time.sleep(1)
print('\nPort-Scan\n	Press Ctrl+C to Canle Scan \n  '+'='*20+'\n')
if len(sys.argv) > 1: target = socket.gethostbyname(sys.argv[1])
else: target = socket.gethostbyname(put)
def scanPort(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c = s.connect_ex((target, port))
    if c == 0: print (' ' + target + ' [+] Port %d \t[open]' % (port,))
    s.close()
for i in range(1, 1024):
    scan = threading.Thread(target=scanPort, args=(target, i))
    scan.start()
