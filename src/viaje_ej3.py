edad = int(input("Dime tu edad en años: "))
niv_fis = int(input("En una escala del 1 al 10 dime tu estado físico (siendo 10 el mejor y 1 el peor): "))

while niv_fis > 10 or niv_fis < 1:
    niv_fis = int(input("Ese número está fuera de la escala. Prueba otra vez: "))

if edad < 18:
    print("Debes ser mayor de edad")
elif niv_fis < 5:
    print("Debes estar en mejor forma")
else:
    print("¡Listo para despegar!")