#Ejercicio 1
mat = input("Nota de mates:\n")
fis = input("Nota de fisica:\n")
quim = input("Nota de quimica:\n")
hs = input("Nota de historia:\n")
leng = input("Nota de lengua:\n")
asignaturas = [
    "Matematicas", mat,
    "Fisica", fis,
    "Quimica", quim,
    "Historia", hs,
    "Lengua", leng
]

#Ejercicio 2
numganador = list()
iteraciones = input("Cuantos numeros tiene el sorteo:\n")
iteraciones = int(iteraciones)
while iteraciones>0:
    n = input("Introduce de izquierda a derecha los numeros del sorteo:\n")
    numganador.append(n)
    iteraciones -= 1
print("Numero ganador: ", numganador)    
numganador.sort()
print("Ordenado: ",numganador)

#Ejercicio 3
asignaturas = [
    "Matematicas", "Fisica", "Quimica", "Historia","Lengua"
]
notas = {
    "Matematicas": 0,
    "Fisica": 0,
    "Quimica": 0,
    "Historia": 0,
    "Lengua": 0
}
for a in asignaturas:
    print("que nota has sacado en %s" % a)
    notas[a] = int(input(">"))
for a in asignaturas:
    if(notas[a] >= 5):
        asignaturas.remove(a)
for a in asignaturas:
    print("Has de recuperar:")
    print(asignaturas)

#Ejercicio 4
palabra = input("Introduzca una palabra:\n")
if palabra == "".join(reversed(palabra)):
    print("Palindromo")
else:    
    print("No palindromo")

#Ejercicio 5
palabra = input("Introduzca una palabra:\n")


#Ejercicio 6


#Ejercicio 7