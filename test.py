import signal
import threading
import time
import sys
import subprocess
import os


proc = None


def mostrarTareas():
    x = subprocess.check_output(
        "ps -A -o stat,user,ppid,pid,cmd --cols 100 | grep '^S\|^R'", shell=True)
    x = x.decode('UTF-8')
    print(x)

def imprimirmenu():
	return '''
	1: Show
	2: Create
	3: Kill
	4: Ver pid ultimo proceso creado
	5: exit
		'''

if __name__ == "__main__":
	print('''
	1: Show
	2: Create
	3: Kill
	4: Ver pid ultimo proceso creado
	5: exit
	''')
	op = int(input())
	while op <= 5 or op > 0:
		uid = os.getuid()
		if op == 1:
			mostrarTareas()
		elif op == 2:
			print(uid)
			result = subprocess.check_output('cut -d: -f1 /etc/passwd', shell=True)
			print(str(result).split("\\n"))
			usuario = int(input("ingrese el UID del usuario\n"))
			juguete.proceso(usuario)
			print("Proceso creado ")
		elif op == 3:
			x = int(input("Ingrese PID: \n"))
			p = os.kill(x, signal.SIGKILL)
			print("Eliminado ")
		elif op == 4:
			print(os.setgid(123))
			try:
				print(proc.pid)
			except:
				print("No se han creado procesos ")
		elif op == 5:
			break
		elif op == 6:
			usuario = str(input("ingrese el nombre del usuario\n"))
			os.system("sudo -u "+usuario+" python3 juguete.py" )
		print(imprimirmenu())
		op = int(input())
#hola