#py
#coding by hendrik
#DoS/DDoS Attack Tool
import socket
import os
##########################
#MAIN MENU DOS SCRIP PY #####
##############################
#LISENSI OPEN SOURCE BEBAS UNTUK #
#MENGEDIT TOOL INI DENGAN CATATAN#
#HARUS MENYERTAKAN NAMA CREATOR#
################################
os.system('clear')
print"""\033[32;1m
=========================================
d8b   db  .o88b. d8888b.  .d88b.  .d8888. 
888o  88 d8P  Y8 88  `8D .8P  Y8. 88'  YP 
88V8o 88 8P      88   88 88    88 `8bo.   
88 V8o88 8b      88   88 88    88   `Y8b. 
88  V888 Y8b  d8 88  .8D `8b  d8' db   8D 
VP   V8P  `Y88P' Y8888D'  `Y88P'  `8888Y' 
=========================================
= DoS Script By Hendrik | Version 1.4   =
=========================================""" #logo menu utama ncdos 
print "\033[34;1mYOUR HOSTNAME/SERVER :", socket.gethostname() #mengambil nama server
print "\033[32;1m========================================="
print "\033[37;1m[1].UDP FLOODER [2].TCP SYN [3].PROXY"
print "\033[32;1m========================================="
select = raw_input("\033[32;1m~NCDOS~#")
#stage2

if select == "1":
    os.system('clear')
    os.system(' sh 1.sh')
elif select == "2":
	os.system('clear')
	os.system('python TCPSYNFLOOD.py')
elif select == "3":
	os.system('clear')
	os.system('python2 D3.py')
else:
	print "MAAF PILIHAN TIDAK TERSEDIA"