import os
def proceso(usuario):
    os.setuid(usuario)
    os.fork()
    print(os.getpid())