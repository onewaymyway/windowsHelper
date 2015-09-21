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
    
def foo(hwnd,mouse):
    global exeDic
    tExe=win32gui.GetWindowText(hwnd)
    if tExe in exeDic:
        pass;
    else:
        exeDic[tExe]=True
        mLog('add:'+tExe)

def exeInfos():
    win32gui.EnumWindows(foo, 0)

def mainLoop():
    while(1):
        exeInfos();
        time.sleep(0.01)
        
if __name__ == "__main__":
    print("args:",sys.argv)
    mainLoop();
