'''Module which contains ftp functions'''

def exit_cmd(**kwargs):
    '''Disconnect from the server'''

    kwargs['ftp'].close()
    exit("Goodbye")

def del_cmd(**kwargs):
    '''Delete something from the server'''

    if len(kwargs['liner']) < 2:
        raise IndexError("Entered too few arguments")

    kwargs['ftp'].delete(kwargs['liner'][1])

def help_cmd():
    '''Help documentation'''

    help_doc = '''
FTP-Shell - Simple and advanced FTP client made by Andreyoss on python3

Command                                        Description
===========================================================

cd <remote-folder>                             Change folder
ls                                             List of all dirs/files
del <remote-file>                              Delete file
help                                           Help reference
exit                                           Goodbye :)
pwd                                            Path to your folder
rename <fromname> <toname>                     Rename file/dir
mkdir <name>                                   Create directory
rmdir <name>                                   Delete directory
    '''

    print (help_doc)

def ls_cmd(**kwargs):
    '''Returns list of available files/dirs'''

    kwargs['ftp'].dir()

def cd_cmd(**kwargs):
    '''Change directory command'''
    if len(kwargs['liner']) < 2:
        raise IndexError("Entered too few arguments")

    kwargs['ftp'].cwd(kwargs['liner'][1])

def pwd_cmd(**kwargs):
    '''Print working directory command'''

    print ("Current directory -", str(kwargs['ftp'].pwd()))

def rename_cmd(**kwargs):
    '''Rename file or directory in the server'''
    if len(kwargs['liner']) < 3:
        raise IndexError("Entered too few arguments")

    kwargs['ftp'].rename(kwargs['liner'][1], kwargs['liner'][2])

def mkdir_cmd(**kwargs):
    '''Make directory command'''
    if len(kwargs['liner']) < 2:
        raise IndexError("Entered too few arguments")

    kwargs['ftp'].mkd(kwargs['liner'][1])

def rmdir_cmd(**kwargs):
    '''Remove directory from the server'''
    if len(kwargs['liner']) < 2:
        raise IndexError("Entered too few arguments")

    kwargs['ftp'].rmd(kwargs['liner'][1])

FUNC_DICT = {
    'exit': exit_cmd,
    'del': del_cmd,
    'help': help_cmd,
    'ls': ls_cmd,
    'pwd': pwd_cmd,
    'rename': rename_cmd,
    'mkdir': mkdir_cmd,
    'rmdir': rmdir_cmd,
    'cd': cd_cmd
}

def exec_cmd(**kwargs):
    '''Execute cmd'''

    if kwargs['liner'][0] in FUNC_DICT:
        try:
            FUNC_DICT[kwargs['liner'][0]](**kwargs)
        except TypeError:
            FUNC_DICT[kwargs['liner'][0]]()

    else:
        similar_cmd = [k for k in FUNC_DICT if k.startswith(kwargs['liner'][0])]
        if similar_cmd:
            print(f"[\x1B[33m?\x1B[37m] Maybe you meant: {', '.join(similar_cmd)}")
        else:
            # Let raise exception if cmd doesn't exist
            raise NameError("Unknown command")
