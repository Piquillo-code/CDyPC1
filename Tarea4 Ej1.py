#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 5 y cuántos menores.
aprobados=0
suspensos=0
for x in range(10):
    nota=int(input("Introduce una nota: "))
    if (nota<5):
        suspensos=suspensos+1
    else:
        aprobados=aprobados+1
print("Aprobados: ",aprobados)
print("Suspensos: ",suspensos)
