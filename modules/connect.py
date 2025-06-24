'''Module for establishing connection with remote server'''

import ftplib

def connect(ftp, host: str, port: int):
    '''Connect function'''

    try:
        ftp.connect(host=host, port=int(port))
    except ftplib.all_errors as e:
        exit("[\x1B[31m-\x1B[37m] "+str(e))
