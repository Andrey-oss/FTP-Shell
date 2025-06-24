'''Print ftp banner'''

BANNER = '''
[\x1B[32m+\x1B[37m] Connected to the FTP Server!
[\x1B[32m+\x1B[37m]                       Server banner                       [\x1B[32m+\x1B[37m]
{0}

{1}

{2}

[\x1B[32m+\x1B[37m] Authentication required\n
'''

def print_banner(ftp):
    '''Print banner'''
    ftp_welcome = ftp.getwelcome()

    print (BANNER.format("-" * 67, ftp_welcome, "-" * 67))
