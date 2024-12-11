'''
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
'''
mas300=0
entre100y300=0
n=int(input("¿Cuántos empleados tiene la empresa? "))
for x in range(n):
    sueldo=int(input("Introduce sueldo "))
    if (sueldo>300):
        mas300=mas300+1
    else:
        if (sueldo>=100):
            entre100y300=entre100y300+1
print("Empleados que ganan más de 300:",mas300)
print("Empleados que ganan entre 100 y 300:",entre100y300)
