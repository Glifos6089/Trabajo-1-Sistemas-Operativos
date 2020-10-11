import subprocess
import os
import signal
import threading
import time
import getch
import sys
import subprocess



proc = None

def mostrarTareas():
	os.system('clear')
	x = subprocess.check_output("ps -e -o stat,user,cmd,pid | grep '^S\|^R'",shell=True)
	x = x.decode('UTF-8')
	print(x)

def desplegarMenu(op):
	if op == 1:
		mostrarTareas()
	elif op == 2:
		result = subprocess.check_output('cut -d: -f1 /etc/passwd', shell=True)
		print(str(result).split("\\n"))
		x = str(input("Ingrese proceso: \n"))
		proc = subprocess.Popen(x, shell=True)
		print("Proceso creado ")
	elif op ==3:
		x = int(input("Ingrese PID: \n"))
		p = os.kill(x, signal.SIGKILL)
		print("Eliminado ")
	elif op == 4:
		if proc:
			print(proc.pid)
		else:
			print("No se han creado procesos ")
	elif op == 5:
		mostrarTareas()

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
	

