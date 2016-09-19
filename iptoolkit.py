#/usr/bin/python
#import requests
import urllib2
import sys
import time as t
from random import randint
#from termcolor import colored
'''
infile = sys.argv[1]
outfile = open("location.csv","w")
csvheader = 'ip,country_code,country_name,region_code,region_name,city,zip_code,time_zone,latitude,longitude,metro_code'
outfile.write(csvheader + "\n")
with open(infile) as f: #Open inputFile as f & loops though lines
		print "\nThe corresponding ascii data are: \n"			
		for ip in f: #Iteration begins, takes line in f
			
			url = 'http://freegeoip.net/csv/'+ip
			webUrl  = urllib2.urlopen(url)
			r= webUrl.read()
			print r #Prints the ascii on screen
			outfile.write(r + "\n")
'''
def dname():
	date = t.localtime(t.time())
	opfname = '%d-%d-%d.csv'%(date[2],date[1],date[0])
	return opfname

opfname = dname()
rid = str(randint(100000, 999999))
outfile = open("ipinfo-" + rid + "-" + opfname ,"w")
csvheader = 'ip,country_code,country_name,region_code,region_name,city,zip_code,time_zone,latitude,longitude,metro_code'

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prBlue(prt): print("\033[94m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))

def banner():
	prCyan("""
	_ ___     ___ ____ ____ _    _    _ ___ 
	| |__]     |  |  | |  | |    |_/  |  |  
	| |        |  |__| |__| |___ | \  |  |  """)
	
	prYellow("""	---------------------------------------""")
	prRed("""	   github.com/ravisankar90/iptoolkit """)
	prGreen("""	       Version 1.0, August - 2016""")
	prYellow("""	---------------------------------------""")
  	
def out(ops,r):
	if ops != "Y" and ops != "y" and ops != "N" and ops != "n":
		prRed("Are you Nuts or can't you read ?")
		ops = "n"
	elif ops == "Y":
		prYellow("\n" + csvheader)#Yellow
		prCyan(r)#Cyan
		print ops
	elif ops == "y":
		prYellow("\n" + csvheader)#Yellow
		prCyan(r)#Cyan
		print ops
	outfile.write(r + "\n")
	
	
		
def main():
	banner()
	prRed("\nSpecify the mode you want to run,")
	prLightPurple("Enter 1 for Single IP")
	prLightPurple("Enter 2 for List of IPs in a file: \n")
	imode = raw_input("Mode: ")
	checkmode(imode)
	mode = imode
	if mode == "1":
		ip = raw_input("Enter Ip address: ")
		prBlue("""Do you want to display results in screen as they come(Verbose Output) ?""")
		ops = raw_input("Yes (Y) No (N): ")
		r = getdata(ip);
		#ops = 'y'
		out(ops,r)
		prGreen("The Output has been saved to ipinfo-"+ rid +"-"+ opfname)
	elif mode == "2":
		prBlue("""Enter the file name with full path of the file which contains list of IPs""")
		prPurple("""eg: /home/user1/Desktop/list.txt""")
		infile = raw_input("File: ")
		prBlue("""Do you want to display results in screen as they come(Verbose Output) ?""")
		ops = raw_input("Yes (Y) No (N): ")
		#ops = 'Y'
		with open(infile) as f: #Open inputFile as f & loops though lines
			for ip in f:
				r=getdata(ip);
				out(ops,r)
		prGreen("The Output has been saved to ipinfo-"+ rid +"-"+ opfname)

def getdata(ip):
	
	url = 'http://freegeoip.net/csv/'+ip
	webUrl  = urllib2.urlopen(url)
	r = webUrl.read()
	return r
	
def checkmode(mode):
	if mode != "1" and mode != "2":
		prRed("Are you Nuts or can't you read ?")
		prRed("Exiting the program...")
		exit()
		
main()
	

