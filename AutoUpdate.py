'''
AutoUpdate(自动更新收藏夹)
'''
from main import update
from time import sleep
import os,sys

def AutoStart():
    '''
    自动启动设置
    '''
    try:
        import win32con,win32api
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',0, win32con.KEY_ALL_ACCESS)
        win32api.RegSetValueEx(key,'Favlist-Saver',0,win32con.REG_SZ,sys.executable)
    except:
        print('添加至启动项失败,请检查程序管理员权限!')

if __name__=='__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'AutoStart':
            AutoStart()
            os._exit(0)
    while True:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        update()
        sleep(3600)