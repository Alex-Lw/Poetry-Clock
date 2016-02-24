#!/usr/bin/env python
# encoding: utf-8
__author__ = 'Alex Luo'
__date__ = '20160131'
import os
import random
import sys
import webbrowser
import time
sys.path.append("libs")

def clocks(duration,commandNum):
    if commandNum==1:
        verse=clearVerse("verse.txt")   #this is the new version which will clear the verse file every time
        words = verse[int(len(verse)*random.random())]
        command = "sleep "+ str(duration)+ " && say '"+words+"'"
        os.system(command)

    if commandNum==2:
        url='http://www.getrelaxed.com'
        time.sleep(duration)
        webbrowser.open(url)

def clearVerse(verseaddress):
    try:
        verse=open(verseaddress).readlines()
    except:
        print "can not open the verse file"
    temp=[]
    for line in verse:
        if len(line)>5:
            if len(line.split('、'))==2:
                temp.append(line.split('、')[1])
            else:
                temp.append(line)
    return temp


if __name__ == '__main__':
    if len(sys.argv)==3:    # if argv==3
        try:
            commandNum=0
            if sys.argv[1]=='-p':
                commandNum=1
            elif sys.argv[1]=='-w':
                commandNum=2
            else:
                raise NameError

            duration = int(sys.argv[2])
            clocks(duration,commandNum)
        except:
            print "error1, please enter it again"
    elif len(sys.argv)==2:
        try:
            duration = int(sys.argv[1])
            clocks(duration,2)
        except:
            print "error2, please enter it again"
    elif len(sys.argv)==1:
        clocks(3600,2)
    else:
        print "error"

