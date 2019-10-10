#(All passwords checked against one user) - one process task 

import time
import sys
import crypt
import multiprocessing

user = []
salt = []
hashes = []
processes = []
starttime = time.time()

def hashverifier(): 
	for i in range(len(salt)):
		p=multiprocessing.Process(target=multi,args=(i,))
		processes.append(p)
		p.start()
	for process in processes:
        	process.join()
				
							
def multi(x):
	print("Started process for user : "+user[x])
	s = salt[x]
	with open(sys.argv[1],'r') as f:
		for line in f:
			passw = line.split()[0]
			output = crypt.crypt(passw,"$6$"+s)			
			if output == hashes[x] :
				print("Found passwd for user "+user[x]+" : "+passw+" in time {} seconds".format(time.time() - starttime))
				return
		pass


with open(sys.argv[2],'r') as f:
	for line in f:
		user.append(line.split(':')[0])
		salt.append(line.split(':')[1].split('$')[2])
		hashes.append(line.split(':')[1])
hashverifier()
pass

print('That took {} seconds'.format(time.time() - starttime))

