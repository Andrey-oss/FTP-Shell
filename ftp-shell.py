from ftplib import FTP
import time
import ftplib
import readline

host = input ("Remote host: ")
port = input ("Remote port: ")

print ("[\x1B[32m+\x1B[37m] Connecting to the FTP Server")

try:
   ftp = FTP(host)
   ftp.connect(host=host, port=int(port))
except ftplib.all_errors as e:
   print ("[\x1B[31m-\x1B[37m] "+str(e))
   exit()

print ("[\x1B[32m+\x1B[37m] Connected to the FTP Server!")
print ("")
print ("[\x1B[32m+\x1B[37m]                       Server banner                       [\x1B[32m+\x1B[37m] ")
print ("--------------------------------------------------------------------")
print ("")
print (ftp.getwelcome())
print ("")
print ("--------------------------------------------------------------------")
print ("")
print ("[\x1B[32m+\x1B[37m] Authentication required")
print ("")
username = input("Please enter username: ")
password = input("Please enter password: ")
print ("[\x1B[32m+\x1B[37m] Trying login to system using "+username+":"+password)
try:
   login = ftp.login(user=username, passwd=password)
   time.sleep(0.5)
   print ("[\x1B[32m+\x1B[37m] Authenfication completed")
   print ("[\x1B[32m+\x1B[37m] Spawning shell")
   time.sleep(1)

except ftplib.all_errors:
   print ("[\x1B[31m-\x1B[37m] User or password incorrect! Exiting..")
   exit()

if login == "230 Login successful":
   print ("[\x1B[32m+\x1B[37m] Authenfication completed")
   print ("[\x1B[32m+\x1B[37m] Spawning shell")
   print ("")
   time.sleep(1)

while True:
      line = input("FTP-Shell:> ")
      liner = line.split()

      try:
         if liner[0] == 'exit':
            print ("Goodbye")
            break

         elif liner[0] == 'delete' or liner[0] == 'del' or liner[0] == 'rm':
            try:
               ftp.delete(liner[1])
               print ("[\x1B[32m+\x1B[37m] Command received successfully!")
            except ftplib.all_errors as e:
               print ("[\x1B[31m-\x1B[37m] "+str(e))

         elif liner[0] == 'dir' or liner[0] == 'ls':
            ftp.dir()

         elif liner[0] == 'cd':
            try:
               ftp.cwd(liner[1])
               print ("[\x1B[32m+\x1B[37m] Command received successfully!")
            except ftplib.all_errors as e:
               print ("[\x1B[31m-\x1B[37m] "+str(e))

         elif liner[0] == 'pwd':
               print ("Current directory - "+str(ftp.pwd()))

         elif liner[0] == 'rename':
               try:
                  ftp.rename(liner[1], liner[2])
                  print ("[\x1B[32m+\x1B[37m] Command received successfully!")
               except ftplib.all_errors as e:
                  print ("[\x1B[31m-\x1B[37m] "+str(e))

         elif liner[0] == 'mkdir' or liner[0] == 'mkd':
               try:
                  ftp.mkd(liner[1])
                  print ("[\x1B[32m+\x1B[37m] Command received successfully!")
               except ftplib.all_errors as e:
                  print ("[\x1B[31m-\x1B[37m] "+str(e))

         elif liner[0] == 'rmdir' or liner[0] == 'rmd':
               try:
                  ftp.rmd(liner[1])
                  print ("[\x1B[32m+\x1B[37m] Command received successfully!")
               except ftplib.all_errors as e:
                  print ("[\x1B[31m-\x1B[37m] "+str(e))

         elif liner[0] == 'help':
            print ("")
            print ("FTP-Shell - Simple and advanced FTP client made by Andreyoss on python3")
            print ("")
            print ("Command                                        Description")
            print ("===========================================================")
            print ("")
            print ("cd <remote-folder>                             Change folder")
            print ("dir/ls                                         List of all dirs/files")
            print ("delete/del/rm <remote-file>                    Delete file/folder")
            print ("help                                           Help reference")
            print ("exit                                           Goodbye :)")
            print ("pwd                                            Path to your folder")
            print ("rename <fromname> <toname>                     Rename file")
            print ("mkd/mkdir <name>                               Create directory")
            print ("rmd/rmdir <name>                               Delete directory")

         else:
            print ("[\x1B[31m-\x1B[37m] Invalid command")

      except Exception as e:
        pass

else:
   print ("[\x1B[31m-\x1B[37m] User cannot be logged in")
   exit()
