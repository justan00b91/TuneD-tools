import re
import os
import time

if os.geteuid() != 0:
    exit("Try with sudo!")

os.system("clear")
tmp = 0
while True:
    profile = []
    for logs in open('/var/log/tuned/tuned.log','r'):
        if "tuned.daemon" in logs:
            line = logs.split("\'")
            if len(line) > 2:
                profile.append(line[1])
    n = len(profile)
    if tmp < n and profile[n-2] != profile[n-1]:
        print("Alert! Tuned profile changed.\n"+profile[n-2]+" -> "+profile[n-1]+"\n")
    tmp = n
    time.sleep(2)

