import re

#Ejercicio 1
saludo = "Hola Juan Perez."
balance = 53.44
print (saludo,"Tu balance es ",balance,"$.")

#Ejercicio 2
pi = 3.14
print(pi,"Tipo: ", type(pi).__name__)
pi = int(pi)
print(pi,"Tipo convertido a: ", type(pi).__name__)
pi = str(pi)
print(pi,"Tipo convertido por segunda vez a: ", type(pi).__name__)

#Ejercicio 3
p = len(saludo)
print(p)

#Ejercicio 4 
saludomayus = saludo.upper()
print(saludomayus)
siono = saludo.startswith("Hola")
print("Contiene Hola el saludo?",siono)

#Ejercicio 5 
quijote = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor». Fuente: «Capítulo primero. Que trata de la condición y ejercicio del famoso hidalgo don Quijote de la Mancha."
patron = "a"
resultado = re.findall(patron, quijote)
print(len(resultado))