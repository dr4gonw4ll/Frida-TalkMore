from os import listdir
from pathlib import Path
import javalang


def listfiles(p):
    fl = listdir(p)
    print(fl)
    return fl

def localparser(s):
    parse = javalang.parse.parse(s)
    return parse.types

def loadparse():
    print('Enter Code Path:')
    path = input()
    fil = listfiles(path)
    for i in fil:
        path_construct = path+'\\'+i
        print(path_construct)
        try:
            f = open(path_construct, 'r')
            retval = localparser(f.read())
            filename = '.cachefile'+str(i)
            f1 = open(filename, 'w')
            f1.write(str(retval))
            f1.close()
        except IOError:
            print('unable to open file'+IOError)
loadparse()