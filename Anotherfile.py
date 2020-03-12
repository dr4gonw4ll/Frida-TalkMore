import AndroidInfo
import Parse
import ast
import re
import platform
import uuid

#location of smali files
smalipath = 'C:\\Users\\anand\\Downloads\\UnCrackable_Level1\\smali\\sg\\vantagepoint\\uncrackable1'

#location of apk
apkpath = "C:\\Users\\anand\\Downloads\\UnCrackable_Level1.apk"

#print('generate Frida handlers here')
#pkgname, fname = AndroidInfo.loadapk()


def getfunandval(x):  #this function returns the function names and the parameter values as list with in the identified values
    #print(x)
    y = re.findall(r'([\w\d]*)\(', str(x[0]))
    z = re.findall(r'\((.*)\)', str(x[0]))
    #print(z[0])
    s = str(z[0]).split(';')
    return y, s


flag = Parse.loadparse(smalipath)
tup = ()
f = open('.\.cachefuntions','r')
fd_script = """ Java.perform(function(){\n\n """
js_file = open('frida_js_file.js', 'w')
js_file.writelines(fd_script)
for i in f.readlines():
    j = ast.literal_eval(i)
    k = list(j.keys())
    l = list(j.values())
    if(len(l[0])>0):
        print(platform.system())
        if(platform.system()=='Windows'):
            class_name = re.findall(r'smali\\(.*)\.smali', str(k[0]))
            class_name = str(class_name[0]).replace('\\', '.')
        else:
            class_name = re.findall(r'smali/(.*)\.smali', str(k[0]))
            class_name = str(class_name).replace(r'/', '.')
        l = l[0]
        for m in l:
            fun_name, fun_val = getfunandval(m)
            print('***********')
            if(fun_val.__contains__('')):
                fun_val = fun_val[:-1]
            else:
                fun_val = fun_val

            js_variable = uuid.uuid4().hex[0:6]
            ret_variable = uuid.uuid4().hex[0:6]
            print(len(fun_val))
            if(len(fun_val)==0):
                funstr = f"""var {js_variable} = Java.use('{class_name}');\n {js_variable}.{fun_name[0]}.implementation = function(){{\nvar {ret_variable} = this.{fun_name[0]}\nconsole.log({ret_variable})\nreturn {ret_variable}\n}}\n"""
                print(funstr)
                js_file.writelines(funstr)
            elif(len(fun_val)==1):
                funstr = f"""var {js_variable} = Java.use('{class_name}');\n {js_variable}.{fun_name[0]}.implementation = function(){{\nvar {ret_variable} = this.{fun_name[0]}\nconsole.log({ret_variable})\nreturn {ret_variable}\n}}\n"""
                print(funstr)
                js_file.writelines(funstr)
            elif (len(fun_val) == 2):
                funstr = f"""var {js_variable} = Java.use('{class_name}');\n {js_variable}.{fun_name[0]}.implementation = function(){{\nvar {ret_variable} = this.{fun_name[0]}\nconsole.log({ret_variable})\nreturn {ret_variable}\n}}\n"""
                print(funstr)
                js_file.writelines(funstr)


