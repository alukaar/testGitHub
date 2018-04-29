print("Ingrese su nombre:")

nombre = input()

print("Ingrese su edad: ")
edad = int(input())


print("Ingrese su estatura(ejem: 1.60):")
estatura = float(input())

print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura,"m")
      

if(edad >= 18):
    print("Mayor de edad")
else:
    if(edad > 18):
        print("Menor de edad")

if(estatura >= 1.50):
    print("Usted es alt@")
else:
    if(estatura < 1.50):
        print("Baja estatura")





