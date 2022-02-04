import re

#Ejercicio 1
a = 50
b = 10
if a>b:
  print("Hello World")

a = 50
b = 10
if a!=b:
  print("Hello World")

a = 50
b = 10
if a==b:
  print("Yes")
else:
  print("No")

a = 50
b = 10
if a == b:
  print("1")
elif a>b:
  print("2")
else:
  print("3")

c = 12
d = 15
if a == b and c == d:
  print("Hello")

if a == b or c == d:
  print("Hello")  

if 5 > 2:
 print("Five is greater than two!")

if 5 > 2: print("Five is greater than two!")  

print("Yes") if 5 > 2 else print("No")

#Ejercicio 2
mayor = 18
edad = input("Edad:\n")
if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Ejercicio 3
contra = "megustanlosenanos"
user = input("Introduce tu contra:\n")
u = user.lower()
if contra == u:
    print("Contra correcta")
else:
    print("Contra incorrecta")

#Ejercicio 4
num = input("Introduce un numero:\n")
n = int(num)
resto = n % 2
if resto == 0:
    print("Par")
else:
    print("Impar")

#Ejercicio 5
num1 = input("Introduce un numero:\n")
num2 = input("Introduce otro numero:\n")
n1 = int(num1)
n2 = int(num2)
if n2 == 0:
    print("Error no se puede dividir por 0")
else:
    resto = n1 % n2
    cociente = n1 / n2
    print(n1," / ",n2," = ", cociente," Resto: ", resto)  

