# import modules
import pythoncom,pyHook
from datetime import datetime

def OnKeyboardEvent(event):
    print (str(datetime.now())) + ' [' + event.WindowName + ']: ' + chr(event.Ascii)
    if (event.Ascii == 27):
       exit(0)
    return event.Ascii

# 1
hook= pyHook.HookManager()
# 2 
hook.keyDown = OnKeyboardEvent    
# 3
hook.HookKeyboard()
# 4
pythoncom.PumpMessages()
