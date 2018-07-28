"""Crea un script llamado descomposicion.py que realice las siguientes tareas:

1.- Debe tomar 1 argumento que será un número entero positivo.
2.- En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:
> 3647

El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:
> 0007
  0040
  0600
  3000"""

import sys
if len(sys.argv) == 2:  #Validación 1
    n = int(sys.argv[1])
    if n < 0 :
        #Mensaje de error 1
        print("Error - Argumentos incorrectos.")
        print("Ejemplo: python descomposicion.py [0-9999999999999999999999999]")
    else:
        #Aquí empieza la lógica del problema
        c = str(n)
        l = len(c)
        for i in range(l):
            print("{c:0{l}d}".format(c=int(c[l-1-i])*10**i,l=l))
else:
    #Mensaje de error 2
    print("Error - Argumentos incorrectos.")
    print("Ejemplo: python descomposicion.py [0-1000]")
