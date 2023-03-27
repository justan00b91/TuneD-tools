import re
import os

if os.geteuid() != 0:
    exit("This program requires sudo!")

if os.path.exists("/etc/system-release-cpe"):
    print("WARNING:File exits at /etc/system-release-cpe\n")

for lines in open("/etc/os-release","r"):
    if re.search("^CPE_NAME*", lines):
        temp = lines.split("=")[1].strip()
        cpe_info = temp[1:len(temp)-1]
        temp = input("Assign role to the system: ")
        if temp:
            sys_role = "::" + temp
            os.system("echo " + cpe_info + sys_role + " > /etc/system-release-cpe")
        else:
            os.system("echo " + cpe_info + " > /etc/system-release-cpe")
        
