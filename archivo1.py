import os
print("el proceso creado tiene el pid: "+ str(os.getpid()) + " donde el usuario que lo creo es el: " + str(os.getuid()))
os.fork()
while(True):
	continue