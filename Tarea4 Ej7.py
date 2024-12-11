'''
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
'''
pares=0
impares=0
n=int(input("Introduce el número de elementos a leer:"))
for x in range(n):
    num=int(input("Introduce un número: "))
    if (num%2==0):
        pares =pares+1
    else:
        impares=impares+1
print("Pares: ",pares)
print("Impares: ",impares)
