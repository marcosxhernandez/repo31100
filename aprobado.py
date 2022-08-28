import sys


if len(sys.argv) !=3:
    print("error necesito 2 argumentos")
else:
        
    primero=float(sys.argv[1])
    segundo=float(sys.argv[2])

    if primero > 10 or primero < 0:
        print("Primero valor no esta entre 0 y 10")
    elif primero >= 7 and segundo >= 7:
        print("promocionado")
    elif primero >= 4 and segundo >= 4:
        print("aprobado, debe rendir final")
    else:
        print("reprobado")