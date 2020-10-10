import subprocess
import os
import signal

print('''
1: Show
2: Create
3: Kill
4: Ver pid ultimo proceso creado
5: exit
''')

op = int(input())
proc = None

while op <= 5 or op > 0:
	if op == 1:
		x = subprocess.check_output("ps -ely",shell=True)
		x = x.decode('UTF-8')
		print(x)
	elif op == 2:
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
		
	print('''
1: Show
2: Create
3: Kill
4: Ver pid ultimo proceso creado
5: exit
	''')
	op = int(input())
	

