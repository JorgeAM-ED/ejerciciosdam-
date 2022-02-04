import os
import os.path

#Ejercicio 1
num = input("Introduce un numero entre 1 y 10:\n")
f = open("tabla"+num+".txt","w")
x = 10
while x != 0:
    f.write(str(num))
    f.write("*")
    num = int(num)
    z = num*x
    f.write(str(x))
    x = int(x)
    f.write(" = ")
    f.write(str(z))
    f.write(os.linesep)
    x -=1
f.close    

#Ejercicio 2
num = input("Introduce un numero entre 1 y 10:\n")
num = str(num)
archivo = "tabla"+num+".txt"
f = open(archivo,"w")
if os.path.isfile(archivo):
    f.open(archivo,"r")
    print(f.read())
    f.close()
else:
    print("El archivo no existe")
