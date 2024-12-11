'''
Realizar un programa que permita cargar dos listas de 5 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
'''
lista1=0
lista2=0
for x in range(5):
    num1=int(input("Introduce un número de la lista 1:"))
    lista1=lista1+num1
for x in range(5):
    num2=int(input("Introduce un número de la lista 2:"))
    lista2=lista2+num2

if (lista1>lista2):
    print("Lista 1 mayor")
else:
     if (lista2>lista1):
         print("Lista 2 mayor")
     else:
        print("Listas iguales")

