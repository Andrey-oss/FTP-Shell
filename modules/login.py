'''Module for connecting to the ftp server'''

import ftplib

def login(ftp, username, password) -> str:
    '''Login function'''

    try:
        resp_code = ftp.login(user=username, passwd=password)

    except ftplib.all_errors:
        exit("[\x1B[31m-\x1B[37m] User or password incorrect! Exiting..")

    return resp_code
