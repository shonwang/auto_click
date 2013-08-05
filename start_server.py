import subprocess
import os

def open_sikuli(p, img):
    """Support sikuli-1.0.0 and sikuli-r930 and Sikuli-r905 in MacOS.
    Need args CURRENT_PATH and IMG_PATH.
    """
    try:
        cmd = p + r'/Sikuli_X/Sikuli-IDE.exe -r %s\start_srv.sikuli --args %s' % (p, img)
        print cmd
        subprocess.Popen(cmd,stdout=subprocess.PIPE)
    except OSError,e:
        print e
        #cmd = r'/Sikuli_X/Sikuli-IDE-1/sikuli-script -r %s/start_srv.sikuli -- %s' % (p, img)
        #subprocess.Popen(cmd.split(' '),stdout=subprocess.PIPE)
    return 0

def close_service():    
    os.system("taskkill /im javaw.exe /f")

current_path = os.getcwd()
open_sikuli(current_path, current_path + r'\images')