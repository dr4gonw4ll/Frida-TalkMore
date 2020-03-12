from pyaxmlparser import APK
import subprocess
import re



def decode(path):
    subprocess.call(['apktool','d', path], stdout=None, stderr=subprocess.STDOUT, shell=True)

def loadapk(p):
    print("Load apk files")
    a = APK(p)
    print('YOOOOOOO')
    print(a.ac)

    getfilename = re.findall(r'([\w\d-]*)\.apk', p)
    decode(p)
    return a.package, getfilename[0]

loadapk()