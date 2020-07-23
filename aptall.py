#!/usr/bin/python3

from sys import argv
import os

class clrs:
    RED="\033[0;31m"
    YELLOW="\033[1;33m"
    GREEN="\033[0;32m"
    BLUE="\033[0;34m"
    BOLD_BLUE="\033[1;34m"
    PURPLE="\033[0;35m"
    LIGHT_RED="\033[1;31m"
    LIGHT_GREEN="\033[1;32m"
    WHITE="\033[1;37m"
    LIGHT_GRAY="\033[0;37m"
    COLOR_NONE="\e[0m"

def parser(txt, i, flag):
    text = str(txt)
    x = text.split(" ", 4)
    if flag == True:
        isInstalled = " [Installed]" if x[0] == "i" else ""
        a = clrs.BLUE + i + ")" + clrs.GREEN + x[2] + clrs.BOLD_BLUE + isInstalled \
                + clrs.LIGHT_GRAY + "\n    " + x[4]
        print(a)
        return x[2]
    else:
        isInstalled = True if x[0] == "i" else False
        a = clrs.BLUE + i + ")" + clrs.GREEN + x[2] + clrs.BOLD_BLUE \
                + clrs.LIGHT_GRAY + "\n    " + x[4]
        if isInstalled == True:
            print(a)
            return x[2]


def inst(appName):
    temp = "/tmp/aptall/temp.txt"
    cmd = "aptitude search " + appName + " > " + temp
    os.system(cmd)

    f = open(temp, "r")
    asd = f.read()
    asd = asd.splitlines()

    length = len(asd)
    i = length
    
    theList = []
    
    for txt in asd:
        theList.append(parser(txt, str(i), True))
        i = i-1
    
    a = -1
    while a > length or a < 0:
        print("\nPlease select what you want to install")
        a = int(input(" >> "))
    
    cmd = "sudo apt install " + theList[length-a]
    os.system(cmd)


def remo(appName):
    temp = "/tmp/aptall/temp.txt"
    cmd = "aptitude search " + appName + " > " + temp
    os.system(cmd)

    f = open(temp, "r")
    asd = f.read()
    asd = asd.splitlines()

    i = 1
    
    theList = []
    
    for txt in asd:
        val = parser(txt, str(i), False)
        if val != None:
            theList.append(val)
            i = i+1
    
    a = -1
    while a > i or a < 0:
        print("\nPlease select what you want to remove")
        a = int(input(" >> "))

    if input("Are you sure [y/N] ") == "y":
        cmd = "sudo apt remove " + theList[a-1]
        os.system(cmd)


def main():
    os.system("mkdir -p /tmp/aptall")
    if len(argv) == 1:
        cmd = "sudo apt update && sudo apt upgrade"
        os.system(cmd)
    elif argv[1][0] != "-":
        inst(argv[1])
    elif argv[1] == "-r" or argv[1] == "-R":
        remo(argv[2])
    elif argv[1] == "-h" or argv[1] == "--help":
        helb = """Usage: aptall [option] <package name>

If there are no options or package name updates and upgrades all packages
If there is only package name without an option then installs the package

Options:
    -h, --help : Prints help
    -r, -R     : Removes given package"""
        print(helb)

try:
    main()
except KeyboardInterrupt:
    print("\nInterrupted")
