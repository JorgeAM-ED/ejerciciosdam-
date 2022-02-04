#Ejercicio 1
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  if i == 3:
      break
  i += 1  

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)  

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)  


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)  

for x in range(6):
  print(x)  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)  

#Ejercicio 2
num = input("Introduce un numero entero positivo:\n")
num = int(num)
i = -1
while i!=num:
    if num == 0:
        print(num)
        num -= 1
    else:
        print(num,",")
        num -= 1  

#Ejercicio 3
num = input("Introduce un numero entero positivo:\n")
num = int(num)
i = -1
while i!=num:
    if num == 0:
        print(num)
        num -= 1
    else:
        print(num,",")
        num -= 1          

#Ejercicio 4
x = 1
y = 1
while x!=11 and y!=11:
    if x == 10:
        y += 1
        x = 1
    else:
        print(x," * ",y," = ",x*y)
        x += 1

#Ejercicio 5
salir = "salir"
eco = input()
while eco != salir:
    print(eco)
    eco = input()