import os

## For load (one min cpu load)

location = "/proc/loadavg"
stat = open(location).read().split()
print("CPU Load-> " + stat[0])

## For disk I/O (this would print read/write count)

location = "/sys/block/"
os.chdir(location)
device = os.listdir()

for disk in device:
    stat = open(location+disk+"/stat","r").read().split()
    print("Disk " + disk + "-> " + stat[0] + "/" + stat[4])

## For network

#location = "/sys/devices/virtual/net/lo/statistics"
#read = open(location+"/rx_bytes").read().strip('\n')
#write = open(location+"/tx_bytes").read().strip('\n')
#print("Network-> "+read+"/"+write)

location = "/sys/class/net/"
os.chdir(location)
device = os.listdir()
for dev in device:
    read = open(location+dev+"/statistics/rx_bytes","r").read().split()
    write = open(location+dev+"/statistics/tx_bytes","r").read().split()
    print("Network " + dev + "-> " + read[0] + "/" + write[0])
