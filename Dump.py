#!/bin/python3
#code=_-udf:8-_
#creater : 

import os,sys
import time
import string,random 

#Main_Menu:-
def Main():
    os.system('clear')
    logo = "'\x1b[1;92m'     _____  _    _ __  __ _____     \n'\x1b[1;92m'   |  __ \| |  | |  \/  |  __ \  \n'\x1b[1;92m'   | |  | | |  | | \  / | |__) |  \n'\x1b[1;92m'   | |  | | |  | | |\/| |  ___/   \n'\x1b[1;92m'   | |__| | |__| | |  | | |    \n'\x1b[1;92m'   |_____/ \____/|_|  |_|_|     \n\n'\x1b[1;91m'   Author      :     Ali     \n'\x1b[1;92m'   Github      :    yaad nahi  \n'\x1b[1;93m'   FB ID       :     Baloch\n'\x1b[1;94m'   TOOL TYPE   :     Random dumping\n'\x1b[1;96m'   WAP NUMBER  :     356            \n"
    
    print(logo)          
    print('\x1b[1;91m This Script Maked By BILAL-HAIDER-ID\n Copyright © : Bilal-XD\n-------------------------------')
    print('\x1b[1;92m[1] Dump Random New UID (10008)')
    print('\x1b[1;93m[2] Dump Random Old UID (100000)')
    print('\x1b[1;97m[0] Exit Menu ')
    Me=input('[•] Choose : ')
    if Me =='1':
        random_new_dump()
    elif Me =='2':
        random_old_dump()
    elif Me =='0':
        exit('[•] Thnx For Use ')
    else:
        print('[×] Choose Correct Option : ');time.sleep(1)
        Main() 
# Create Def fb new auto_random uid dump --
def random_new_dump():
    print('-------------------------------')
    try:
        user = []
        print("[*] Enter First 6 digit of any UID")
        print ("\x1b[1;91m[*] file name example \x1b[1;97m /sdcard/ali_new.txt")
        print("\x1b[1;92m[*] 100000   100010  100020")
        print("\x1b[1;93m[*] 100083   100084  100085")
        user_id = input("[*] Enter Digit User ID : ")
        save_file = input("[*] Dump File Save As : ")
        if len(user_id)==6:
            code = user_id
        elif len(user_id)>6:
            code = user_id[:6]
        else:
            print("Wrong User Input")
            exit()
        limit = int(input("[*] Enter Dump Limit : "))
        if (limit)>5000:
            limit = 5000
        for number in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(9))
            user.append(nmp)
        dumpp = open(save_file,'w')
        for bilal in user:
            uid = code+bilal
            dumpp.write(uid+' | '+'ALI_RANDOM_DUMP'+'\n')
            print(uid+' | '+'ALI_RANDOM_DUMP')
            time.sleep(0.05)
        dumpp.close()
        print("Dumping Done ")
        print(f"Your File Save As {save_file}")
    except Exception as e:
        print(e)

def random_old_dump():
    print('-------------------------------')
    try:
        user = []
        print("[*] Enter First 6 digit of any UID")
        print ("\x1b[1;91m[*] file name example \x1b[1;97m /sdcard/ali_new.txt")
        print("\x1b[1;93m[*] 1000000   10000000  100000000")
        user_id = input("[*] Enter Digit User ID : ")
        save_file = input("[*] Dump File Save As : ")
        if len(user_id)==6:
            digitt = 9
        elif len(user_id)==7:
            digitt = 8
        elif len(user_id)==8:
            digitt = 7
        elif len(user_id)==9:
            digit = 6
        else:
            print("Wrong User Input")
            exit()
        code = user_id
        limit = int(input("[*] Enter Dump Limit : "))
        if (limit)>5000:
            limit = 5000
        for number in range(limit):
            nmp = ''.join(random.choice(string.digits) for _ in range(digitt))
            user.append(nmp)
        dumpp = open(save_file,'w')
        for bilal in user:
            uid = code+bilal
            dumpp.write(uid+' | '+'ALI_RANDOM_DUMP'+'\n')
            print(uid+' | '+'ALI_RANDOM_DUMP')
            time.sleep(0.05)
        dumpp.close()
        print("Dumping Done ")
        print(f"Your File Save As {save_file}")
    except Exception as e:
        print(e)
Main()
