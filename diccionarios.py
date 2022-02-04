from importlib.resources import read_text
from pickletools import read_string1
from tkinter import READABLE

#Ejercicio 1

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020;

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#Ejercicio 2
divisas = {
  "Euro": "€",
  "Yen": "¥",
  "Dolar": "$",
}
mensaje=input('Que divisa busca?\n')
if mensaje in divisas: print(divisas[mensaje])
else:
  print("No se ha encontrado esa divisa.")

#Ejercicio 3
nom = input("Introduzca su nombre:\n")
edad = input("Introduzca su edad:\n")
dir = input("Introduzca su direccion:\n")
tel = input("Introduzca su telefono:\n")
datos = {
  "Nombre": nom,
  "Edad": edad,
  "Direccion": dir,
  "Telefono": tel,
}
print(datos.get("Nombre"),"tiene ", datos.get("Edad")," años, vive en ", datos.get("Direccion")," y su numero es ",datos.get("Telefono"))

#Ejercicio 4
frutas = {
  "Platano": 1.88,
  "Manzana": 2.55,
  "Naranja": 4.68,
}
frut = input("Introduzca el nombre de la fruta deseada:\n")
if frut in frutas: 
    print("Fruta en el inventario.")
    precio = frutas.get(frut)
    print("Su precio es de: ",precio," €\n")
    kilos = float(input("Kg a comprar:\n"))
    preciototal = precio*kilos
    print("Son ",preciototal," € en total.")
else:
  print("Fruta no disponible.")  