# !/usr/bin/python3
import subprocess
import os
import time
import random
from colorama import Fore


def check_root():
    print(Fore.YELLOW + "\n--------------------------------------------------")
    print(Fore.GREEN + "[INFO] " + Fore.BLUE + "CHECKING ROOT STATUS\n")
    devl = 26
    #get connected device status
    device = subprocess.check_output('adb devices', shell=True)
    paths = ["/system/sd/xbin/su","/system/bin/failsafe/su","/system/app/Superuser.apk",
          "/data/local/xbin/su","/data/local/bin/su","/system/priv-app/Superuser.apk",
         "/system/priv-app/superuser.apk","/system/app/superuser.apk","/sbin/su","/system/bin/su",
         "/system/xbin/su","/data/local/su","/su/bin/su"]
    #check if device is connected
    if len(device) is not devl:
        #iterate over path and check if path exists on device
        for path in paths:
            cmd = "adb shell 'if [ -f " + path + " ];then echo 1; else echo 0; fi'"
            check = subprocess.check_output(cmd, shell=True)
            if check is 1:
                print("\t[+] Device is rooted")
                break
        print(Fore.GREEN+"\t[-] Device is not rooted")
    elif len(device)  is devl:
        print(Fore.RED+"\t[!] Device is not connected")
    else:
        print(Fore.RED+"\t[!]Check if adb is installed  ")



def main():
    fonts = ["bubble","digital","ivrit","mini","script","shadow","slant","small","smscript","smshadow","smslant","standard"]
    random.shuffle(fonts)
    os.system("clear")
    print(Fore.BLUE)
    os.system(f"figlet -f {fonts[random.randint(0, len(fonts)-1)]} CheckRoot ")
    print(Fore.BLUE + "\t\t\tCreated By W1nterFr3ak")
    print(Fore.YELLOW + "\t\tWinter says knowing  if you are root is power")
    print(Fore.GREEN + "\t\tMail: WinterFreak@protonmaail.com ")
    print()
    check_root()

if __name__ == "__main__":
    main()