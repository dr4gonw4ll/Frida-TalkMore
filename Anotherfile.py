import AndroidInfo
import Parse

#location of smali files
smalipath = 'C:\\Users\\anand\\Downloads\\UnCrackable_Level1\\smali\\sg\\vantagepoint\\uncrackable1'

#location of apk
apkpath = "C:\\Users\\anand\\Downloads\\UnCrackable_Level1.apk"

#print('generate Frida handlers here')
#pkgname, fname = AndroidInfo.loadapk()

flag = Parse.loadparse(smalipath)
f = open('.\.cachefuntions','r')
for i in f.readlines():



