import os
import win32api
import time
import win32gui
import sys
import platform
import ctypes
import winproc

exeDic={}

ISOTIMEFORMAT="%Y-%m-%d %X"
def mLog(msg):
    print(time.strftime(ISOTIMEFORMAT, time.localtime()))
    print(msg)
def exeInfos():
    global exeDic
    procList = winproc.getProcList()
    pList={}
    for pp in procList:
        tExe=pp.szExeFile.decode('gbk')
        if tExe in exeDic:
            pass;
        else:
            exeDic[tExe]=True
            mLog('add:'+tExe)

def mainLoop():
    while(1):
        exeInfos();
        time.sleep(0.1)
    
    
    

if __name__ == "__main__":
    print("args:",sys.argv)
    mainLoop();

       

