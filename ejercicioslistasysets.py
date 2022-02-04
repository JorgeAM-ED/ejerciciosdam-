#ejercicio 1
from asyncore import read


fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

fruits = ("apple", "banana", "cherry")
print(fruits[0])

#ejercicio 2
asignaturas = ["Matematicas","Fisica","Quimica","HIstoria","Lengua"]
print(asignaturas)

#ejercicio 3
for i in asignaturas:
    print("Yo estudio",i)

#ejercicio 4
#Los sets no pueden tener elementos repetidos

#ejercicio 5
numero = [1,2,3]
cadenas = ["Hola","mundo"]
numero.append(4)
cadenas.append("Adios")

#ejercicio 6
a = ["Jake", "John", "Eric"]
b= ["John", "Jill"] 
print(a&b)

#ejercicio 7
lista = {1*1,2*2,3*3,4*4,5*5}