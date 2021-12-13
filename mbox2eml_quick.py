#!/usr/bin/python2

import re, sys, os, uuid

def emls(f):
	mbox = open(f).read()
	if "From " not in mbox[0:10]: return 0
	
	mbox = "\n" + mbox + "\nFrom "
	dir = f+".dir/"
	
	try: os.mkdir(dir)
	except: pass

	i = 0
	for eml in re.findall("\n(From .*?)(?=\nFrom )", mbox, re.DOTALL):
		try: target = re.sub("[^\w]+", "_", re.findall("[dD]{1}[aA]{1}[tT]{1}[eE]: .*?(\d+[^\n]+)", eml)[0]).strip("_")+".eml"
		except: target = str(uuid.uuid4())+".eml"
		
		if os.path.isfile(os.path.join(dir, target)):
			if not os.path.isdir(os.path.join(dir, "duplicate")): os.mkdir(os.path.join(dir, "duplicate"))
			target = os.path.join(dir, "duplicate", target)
		else:
			target = os.path.join(dir, target)
			
		open(target, "w").write(eml)
		i += 1
	
	return i

if 1 == len(sys.argv):
	for filename in os.listdir(os.getcwd()):
		mb = os.path.join(os.getcwd(), filename)
		if os.path.isfile(mb):
			n = emls(mb)
			if n: print mb + " ... yes, mbox (" + str(n) + ")"
else:
	emls(os.path.join(os.getcwd(), sys.argv[1]))
