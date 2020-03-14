# Frida-Talkmore

Frida-TalkMore is to know more about Android application internals. It is a Python3 script. Just provide it with root of smali files directory and it will generates equivalent Frida handler .js script. This script reads all the functions of Android .smali code which returns some object. The object is printed by Frida-TalkMore to the console making the application more verbose and learn more about application.

<h5>Usage:
>python talkmore.py \<path to smali files\>

This script has not been tested on any *nix machines. I have only used it on Windows.