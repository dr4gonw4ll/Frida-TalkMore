# Frida-Talkmore

Frida-TalkMore is to know more about Android application internals. It is a Python3 script. Just provide it with root of smali files directory and it will generates equivalent Frida handler .js script. This script reads all the functions of Android .smali code which returns some object. The object is printed by Frida-TalkMore to the console making the application more verbose and learn more about application.

This script has not been tested on any *nix machines. I have only used it on Windows.
<h5>Usage:</h5>   
1. Decode the apk with apktool
2. Copy the smali directory path for which you want to generate Frida handler code
3. The script will automatically walk through the provided root directory
```python talkmore.py C:\Users\Downloads\UnCrackable_Level1\smali\sg\vantagepoint```
