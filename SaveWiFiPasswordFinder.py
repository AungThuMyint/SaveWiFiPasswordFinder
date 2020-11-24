import platform
import subprocess
import os
from colorama import Fore, Back, Style

banner = """
    ___                __      ___ ___ _   ___                              _   ___ _         _
    / __| __ ___ _____  \ \    / (_) __(_) | _ \__ _ _______ __ _____ _ _ __| | | __(_)_ _  __| |___ _ _
    \__ \/ _` \ V / -_)  \ \/\/ /| | _|| | |  _/ _` (_-<_-< V  V / _ \ '_/ _` | | _|| | ' \/ _` / -_) '_|
    |___/\__,_|\_/\___|   \_/\_/ |_|_| |_| |_| \__,_/__/__/\_/\_/\___/_| \__,_| |_| |_|_||_\__,_\___|_|

        Coder By : h4n24wnyin3 & 4un97huMy!n7
"""
exit_tool = """
  ,---. .           ,         ,--.           .  .                  ,-.            ,---.         . 
    |   |           |         |              |  |     o           /   \             |           | 
    |   |-. ,-: ;-. | , ,-.   |-   ,-. ;-.   |  | ,-. . ;-. ,-:   |   | . . ;-.     |   ,-. ,-. | 
    |   | | | | | | |<  `-.   |    | | |     |  | `-. | | | | |   \   / | | |       |   | | | | | 
    '   ' ' `-` ' ' ' ` `-'   '    `-' '     `--` `-' ' ' ' `-|    `-'  `-` '       '   `-' `-' ' 
                                                          `-'                                   
                                                                    Bye Bye ...
"""
### OS Detect ###
OperatingSystem = platform.system()
print(Style.BRIGHT + Fore.YELLOW + banner)
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.GREEN)
print("###########################################")
print("Platform : "+ OperatingSystem)
print("###########################################")

if OperatingSystem == "Windows" :
    data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    wifis = [line.split(':')[1][1:-1] for line in data if  "All User Profile" in line]
    for wifi in wifis:
            results = subprocess.check_output(['netsh','wlan','show','profile',wifi,'key=clear']).decode('utf-8').split('\n')
            results = [line.split(':')[1][1:-1] for line in results if "Key Content" in  line]   
            for Pass in results:
                print("Name     : "+ wifi+"\nPassword : "+ Pass)

elif OperatingSystem == "Linux" :
    os.chdir(r"/etc/NetworkManager/system-connections") 
    data = os.listdir("/etc/NetworkManager/system-connections")
    for wifi in data:
        results = subprocess.check_output(['sudo','cat',wifi]).split('\n')
        results = [line.split(":") for line in results if "psk=" in  line] 
        for a in results:
            for Pass in a:
                print("\nName     :  " + wifi +" \nPassword : " + Pass +"\n")

else:
   print("Can't Detect Platform ")

print("###########################################")
print(Style.RESET_ALL)
print(Style.BRIGHT + Fore.RED + exit_tool)