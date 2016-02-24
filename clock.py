#!/usr/bin/env python
# encoding: utf-8
__author__ = 'Alex Luo'
__date__ = '20160131'
import os
import random
import sys

def clocks(duration):
    #verse = open("verse.txt").readlines()          #this is old version for assume that the verse file is regular
    verse=clearVerse("verse.txt")   #this is the new version which will clear the verse file every time
    words = verse[int(len(verse)*random.random())]
    command = "sleep "+ str(duration)+" && open /Applications/Safari.app http://www.getrelaxed.com/"
    #command = "sleep "+ str(duration)+ " && say '"+words+"'"
    os.system(command)

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
    if len(sys.argv)!=1:
        try:
            duration = int(sys.argv[1])
            clocks(duration)
        except:
            print "error, please enter it again"
    else:
        clocks(3600)

