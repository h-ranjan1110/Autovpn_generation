
import datetime
import os
import io

print("Which day is this when you are running the script")
print("Enter it in following format\n")
print("If it is Sunday    : Enter 0")
print("If it is Monday    : Enter 1")
print("If it is Tuesday   : Enter 2")
print("If it is Wednesday : Enter 3")
print("If it is Thursday  : Enter 4")
print("If it is Friday    : Enter 5")
print("If it is Saturday  : Enter 6")
day=input("Enter The Appropriate Number :")
print("Paste here the complete path to the vpn.py file")
path=raw_input()
t=datetime.datetime.time(datetime.datetime.now())
hr=int(t.hour)+1
min=int(t.minute)+35
min=min%60
hr=hr%24
log=str(min)+" "+str(hr)+" "+"*"+" "+"*"+" "+str(day)+" "+"python"+" "+path


os.system("python"+" "+"vpn.py")

f=open("cron_list.txt","w+")
f.write(log)

f.seek(0,2)

f.close()

