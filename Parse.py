from os import listdir
from pathlib import Path
import javalang
import re


def listfiles(p):
    fl = listdir(p)
    #print(fl)
    return fl

"""def enumerator(lvalue):
    print('enum function call')
    s4 = re.findall(r'\.method.*(a\([\S]*\)).*\.locals', lvalue)
    print(s4)
    return s4"""

def reparser(s): #this function parses the function names in the files
    match = re.findall(r'\n', s)
    s1 = s.replace('\n', ' ')
    s2 = s1.replace('.method', '\n.method')
    s3 = re.findall('(\.method.*return( |-)(?!void).*\.end method)', s2) #retrieves all the functions which has return
    s6 = ''
    for i in s3:
        s6 = re.findall(r'\.method.*([\S]{1,}\([\S]*\)).*\.locals', str(i)) # lists out all the functions which returns some value May change if method name has special chars
        print(s6)
    return s6

def loadparse(): #this function locates all the files and pushes the files info to reparse() function
    print('Enter Code Path:')
    #path = input()
    path = 'C:\\Users\\anand\\Downloads\\UnCrackable-Level1\\smali\\sg\\vantagepoint\\a'
    fil = listfiles(path)
    for i in fil:
        path_construct = path+'\\'+i
        #print(path_construct)
        try:
            f = open(path_construct, 'r')
            filename = '.cachefile-' + str(i)
            retval = reparser(f.read())
            f1 = open(filename, 'w')
            f1.write(str(retval))
            f1.close()
        except IOError:
            print('unable to open file'+IOError)
loadparse()