from os import listdir
from pathlib import Path
import javalang


def listfiles(p):
    fl = listdir(p)
    print(fl)
    return fl


def loadparse():
    print('Enter Code Path:')
    path = input()
    fil = listfiles(path)
    for i in fil:
        path_construct = path+'\\'+i
        print(path_construct)
        try:
            f = open(path_construct, 'r')
            print(f.read())
        except IOError:
            print('unable to open file'+IOError)
loadparse()