import signal
import threading
import time
import sys
import subprocess
import os

proc = None

from os import scandir, getcwd

def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

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
	5: exit
		'''

if __name__ == "__main__":
	print('''
	1: Show
	2: Create
	3: Kill
	5: exit
	''')
	op = int(input())
	contador=0
	while op <= 5 or op > 0:
		uid = os.getuid()
		if op == 1:
			mostrarTareas()
		elif op == 2:
			print("presione 1 para crear procesos padres(solo se puede crear un proceso hijo del padre que se crea")
			a = int(input())
			if a == 1:
					print("presione 1 si desea crear un proceso hijo del proceso, de lo contrario presione 0 (solo se creara el padre\n pues no logramos hacer que se pueda crear un hijo despues de crear el padre :c")
					b=int(input())
					if(b == 0):
						contseted= str(contador)
						print(uid)
						result = subprocess.check_output('cut -d: -f1 /etc/passwd', shell=True)
						print(str(result).split("\\n"))
						usuario = input("ingrese el nombre del usuario\n")
						os.system('su '+usuario+' -c "touch archivo'+contseted+'.py"')
						archivo = open("archivo"+contseted+".py","w")
						archivo.write("""import os
print("el proceso creado tiene el pid: "+ str(os.getpid()) + " donde el usuario que lo creo es el: " + str(os.getuid()))
while(True):
	continue""")
						archivo.close()
						hola = os.system('su '+usuario+' -c "python3 archivo'+contseted+'.py &"')
						#os.system('su '+usuario+' -c "nano archivo'+contseted+'.txt"')
						contador+=1
						print("Proceso creado ")
					else:
						contseted= str(contador)
						print(uid)
						result = subprocess.check_output('cut -d: -f1 /etc/passwd', shell=True)
						print(str(result).split("\\n"))
						usuario = input("ingrese el nombre del usuario que quiere que cree el padre y el hijo\n")
						os.system('su '+usuario+' -c "touch archivo'+contseted+'.py"')
						archivo = open("archivo"+contseted+".py","w")
						archivo.write("""import os
print("el proceso creado tiene el pid: "+ str(os.getpid()) + " donde el usuario que lo creo es el: " + str(os.getuid()))
os.fork()
while(True):
	continue""")
						archivo.close()
						os.system('su '+usuario+' -c "python3 archivo'+contseted+'.py &"')
						#os.system('su '+usuario+' -c "nano archivo'+contseted+'.txt"')
						contador+=1
						print("Proceso creado junto con su hijo\n")
		elif op == 3:
			x = int(input("Ingrese PID: \n"))
			p = os.kill(x, signal.SIGKILL)
			print("Eliminado ")
		elif op == 5:
			break
		print(imprimirmenu())
		op = int(input())
#hola