import subprocess
import os
import signal
import threading
import time
import sys
import subprocess



proc = None

def mostrarTareas():
	os.system('clear')
	x = subprocess.check_output("ps -A -o stat,user,ppid,pid,cmd --cols 100",shell=True)
	x = x.decode('UTF-8')
	print(x)

def desplegarMenu(op):
	if op == 1:
		mostrarTareas()
	elif op == 2:

		# Get the real user ID 
		# of the current process 
		# using os.getuid() method 
		uid = os.getuid() 
		
		# Print the real user ID 
		# of the current process 
		print("Real user ID of the current process:", uid) 
		
		# Set real user ID 
		# of the current process 
		# using os.setuid() method 
		#uid = 1001
		#os.setuid(uid) 
		#print("Real user ID changed") 
		
		
		# Print the real user ID 
		# of the current process 
		print("Real user ID of the current process:", os.getuid()) 

		
		result = subprocess.check_output('cut -d: -f1 /etc/passwd', shell=True)
		print(str(result).split("\\n"))
		x = str(input("Ingrese proceso: \n"))
		proc = subprocess.Popen(x,shell=True,user=1001)
		print("Proceso creado ")
	elif op ==3:
		x = int(input("Ingrese PID: \n"))
		p = os.kill(x, signal.SIGKILL)
		print("Eliminado ")
	elif op == 4:
		print(os.setgid(123))
		try:
			print(proc.pid)
		except:
			print("No se han creado procesos ")

if __name__ == "__main__":
	op = 1
	while(op != 5):
		print('''
1: Show
2: Create
3: Kill
4: Ver pid ultimo proceso creado
5: exit
		''')
		op = int(input())
		desplegarMenu(op)
	

