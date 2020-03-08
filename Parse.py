from os import listdir, walk
from pathlib import Path
import re


def getallfiles(p):
    fileslist = []
    fname = []
    for root, direc, filename in walk(p, topdown=True):
        for i in filename:
            fileslist.append(root+"\\"+i)
    return fileslist


def getretrunfunctions(s): #this function parses the function names in the files
    funret = []
    match = re.findall(r'\n', s) # finds if new line is present, to make if condition for linux and windows new line chars \r\n and \n
    s1 = s.replace('\n', ' ') #replacing all the new lines, to be updated for linux as well \r\n and \n for linux
    s2 = s1.replace('.method', '\n.method') #push all the methods to new line for easy regular expression check
    s3 = re.findall('(\.method.*return( |-)(?!void).*\.end method)', s2) #retrieves all the functions which has return
    s6 = ''
    for i in s3:
        s6 = re.findall(r'([\S]*\([\w\S]*\)).*\.local', str(i)) # lists out all the functions which returns some value May change if method name has special chars
        funret.append(s6)
    return funret


def getAllFunctions():
    return True


def loadparse(path): #this function locates all the files and pushes the files info to reparse() function
    print('Enter Code Path:')
    fpath = getallfiles(path)
    flag = True
    f1 = open('.cachefuntions', 'w')
    for i in fpath:
        dit = {}
        try:
            f = open(i, 'r')
            dit.__setitem__(i, getretrunfunctions(f.read()))
            f1.writelines(f'{dit}')
            f.close()
        except IOError:
            print('unable to open file'+IOError)
            flag = False
    f1.close()
    return flag
