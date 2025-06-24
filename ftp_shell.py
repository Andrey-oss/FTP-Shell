'''FTP-shell main file'''

# Readline gives us ability to edit/return to the commands entered before and right now
import readline
import ftplib
from ftplib import FTP
from modules.login import login
from modules.connect import connect
from modules.banner import print_banner
from modules.commands import exec_cmd

HOST = str(input ("Remote host: "))
PORT = int(input ("Remote port: "))

print ("[\x1B[32m+\x1B[37m] Connecting to the FTP Server")

ftp = FTP(HOST)

connect(ftp, HOST, PORT)

print_banner(ftp)

username = input("Please enter username: ")
password = input("Please enter password: ")

print (f"[\x1B[32m+\x1B[37m] Trying login to system using {username}:{password}")
login_resp_code = login(ftp, username, password)

if "230 Login successful" in login_resp_code:
    print ("[\x1B[32m+\x1B[37m] Authentication completed")
    print ("[\x1B[32m+\x1B[37m] Spawning shell")
    print ("")
else:
    exit("[\x1B[31m-\x1B[37m] User cannot be logged in")

while True:
    line = input("FTP-Shell:> ")
    liner = line.split()

    try:
        if liner:
            data = {'ftp': ftp, 'liner': liner}
            exec_cmd(**data)
    except ftplib.all_errors as e:
        print ("[\x1B[31m-\x1B[37m] "+str(e))
    except NameError:
        print ("[\x1B[31m-\x1B[37m] Unknown command")
    except IndexError:
        print ("[\x1B[31m-\x1B[37m] Too few arguments entered")
    else:
        print ("[\x1B[32m+\x1B[37m] Command received successfully!")
