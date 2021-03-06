#!/usr/bin/python3

import sys
import os
import argparse

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


def upgr(*args):
    cmd = "sudo apt update && sudo apt upgrade"
    os.system(cmd)


def parser(txt, i):
    text = str(txt)
    x = text.split(" ", 4)
    if i != "-1":
        isInstalled = " [Installed]" if x[0] == "i" else ""
        a = clrs.BLUE + i + ")" + clrs.GREEN + x[2] + clrs.BOLD_BLUE + isInstalled \
                + clrs.LIGHT_GRAY + "\n    " + x[4]
        print(a)
        return x[2]
    else:
        isInstalled = True if x[0] == "i" else False
        a = ")" + clrs.GREEN + x[2] + clrs.BOLD_BLUE \
                + clrs.LIGHT_GRAY + "\n    " + x[4]
        if isInstalled == True:
            return (a, x[2])


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
        theList.append(parser(txt, str(i)))
        i = i-1
    
    theList.reverse()

    print("\nPlease select what you want to install. Ex: 1 | 1 2 3 | 1-4")
    a = str(input(" >> "))

    appList = []

    if '-' in a:
        a = a.split('-')
        for index in range( int(a[0]), int(a[1]) ):
            appList.append(theList[ index-1 ])
        apps = " ".join(appList)
    else:
        a = a.split()
        for index in a:
            appList.append(theList[ int(index)-1 ])
        apps = " ".join(appList)

    
    cmd = "sudo apt install " + apps
    os.system(cmd)


def remo(appName):
    temp = "/tmp/aptall/temp.txt"
    cmd = "aptitude search " + appName + " > " + temp
    os.system(cmd)

    f = open(temp, "r")
    asd = f.read()
    asd = asd.splitlines()

    theList = []
    
    for txt in asd:
        val = parser(txt, "-1")
        if val != None:
            theList.append(val)

    length = len(theList)

    for i, txt in enumerate(theList):
        print(clrs.BLUE + str(length-i) + theList[i][0])
    
    print("\nPlease select what you want to remove. Ex: 1 | 1 2 3 | 1-4")
    a = str(input(" >> "))

    appList = []

    theList.reverse()

    if '-' in a:
        a = a.split('-')
        for index in range( int(a[0]), int(a[1]) ):
            appList.append(theList[ index-1 ][1])
        apps = " ".join(appList)
    else:
        a = list(a.split())
        for index in a:
            appList.append(theList[ int(index)-1 ][1])
        apps = " ".join(appList)

    cmd = "sudo apt remove " + apps
    os.system(cmd)


def autoremo(*args):
    cmd = "sudo apt autoremove"
    os.system(cmd)


def fromfile(fileName):
    f = open(fileName, "r")
    asd = f.read()
    asd = asd.splitlines()
    
    cmd = "sudo apt install " + ' '.join(asd)
    os.system(cmd)


def main():
    os.system("mkdir -p /tmp/aptall")
    
    parse = argparse.ArgumentParser()
    
    parse.add_argument("package", metavar="<Package Name>",
            nargs='?', help="Name of the package")
    parse.add_argument("-i", "--install",
            dest='funcs', action="append_const", const=inst,
            help="Install the given package, same as 'aptall <package name>'")
    parse.add_argument("-r", "--remove",
            dest='funcs', action='append_const', const=remo,
            help="Remove the given package")
    parse.add_argument("-a", "--autoremove",
            dest='funcs', action="append_const", const=autoremo,
            help="Remove unused packages")
    parse.add_argument("-u", "--upgrade",
            dest='funcs', action="append_const", const=upgr,
            help="Upgrade packages, same as using without argument")
    parse.add_argument("-f", "--file",
            dest='funcs', action="append_const", const=fromfile,
            help="Read package names from given file, separated by lines and download them")

    args = parse.parse_args()
    if not args.package:
        if not args.funcs:
            upgr()
        else:
            for func in args.funcs:
                if func.__name__ != "upgr" and func.__name__ != "autoremo":
                    sys.exit("Wrong usage, please check help page: aptall -h")
                func()
    else:
        if not args.funcs:
            inst(args.package)
        else:
            for func in args.funcs:
                func(args.package)


try:
    main()
except KeyboardInterrupt:
    print("\nInterrupted")
