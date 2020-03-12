import parsebytecode
import ast
import re
import platform
import random
import sys
import string


def getfunandval(x):  # this function returns the function names and the parameter values as list with in the identified values
    # print(x)
    y = re.findall(r'([\w\d\$]*)\(', str(x[0]))
    z = re.findall(r'\((.*)\)', str(x[0]))
    # print(z[0])
    s = str(z[0]).split(';')
    return y, s


def generatescript(smalipath):  # writes frida generated script
    flag = parsebytecode.loadparse(smalipath)
    tup = ()
    stat = True
    f = open('.\.cachefuntions', 'r')
    fd_script = """ Java.perform(function(){\n """
    js_file = open('frida_talkmore.js', 'w')
    js_file.writelines(fd_script)
    for i in f.readlines():
        j = ast.literal_eval(i)
        k = list(j.keys())
        l = list(j.values())
        if (len(l[0]) > 0):
            if (platform.system() == 'Windows'):
                class_name = re.findall(r'smali\\(.*)\.smali', str(k[0]))
                class_name = str(class_name[0]).replace('\\', '.')
            else:
                class_name = re.findall(r'smali/(.*)\.smali', str(k[0]))
                class_name = str(class_name).replace(r'/', '.')
            print('Class Name: '+str(class_name))
            l = l[0]
            for m in l:
                fun_name, fun_val = getfunandval(m)
                print('Function Name: '+str(fun_name))
                if (fun_val.__contains__('')):
                    fun_val = fun_val[0:-1]
                js_variable = ''.join(random.choice(string.ascii_letters) for i in range(8))
                ret_variable = ''.join(random.choice(string.ascii_letters) for i in range(8))
                variable_ids = map(lambda x: ''.join(random.choice(string.ascii_letters) for i in range(8)), fun_val)
                tup = tuple(list(variable_ids))
                if (len(
                        tup) == 1):  # to fix python list conversion to tuple, single argument structure https://wiki.python.org/moin/TupleSyntax
                    tup = str(tup).replace(',', '')
                final_var = str(tup).replace('\'', '')
                final_var_toprint = final_var.replace('(', '')
                final_var_toprint = final_var_toprint.replace(')', '')
                # print(final_var)
                funstr = f"""var {js_variable} = Java.use('{class_name}');\n {js_variable}.{fun_name[0]}.implementation = function{final_var}{{\nconsole.log('Class Name: {class_name}')\nconsole.log('Variable Values',{final_var_toprint})\nvar {ret_variable} = this.{fun_name[0]}{final_var}\nconsole.log({ret_variable})\nreturn {ret_variable}\n}}\n"""
                js_file.writelines(funstr)
    print('..........................')
    js_file.writelines('});')
    js_file.close()
    return True

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        desc = """Frida-TalkMore is a simple program which reads .smali files bytecode and generates equivalent Frida dynamic instrumentation .js script. This script reads all the functions of Android .smali code which returns some object. The object is printed by Frida-TalkMore to the console making the application more verbose and learn more about application"""
        usage = """\n\n\nPython3\n\n--usage:\npython talkmore.py <.smali code path>\ne.g. python talkmore.py C:\\Users\\user\Downloads\\UnCrackable_Level1\\smali\\sg\\vantagepoint\\uncrackable1"""
        print(desc+usage)
    elif(sys.argv[1].__contains__('smali')):
        if(generatescript(sys.argv[1])==True):
            print('check the frida-talkmore.js script in the current directory')
    else:
        print('Please pass the .smali code path properly')
