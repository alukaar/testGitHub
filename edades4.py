

vuelta = 0

limite = int(input("¿Cuantas personas serán?: "))


while(True):

    vuelta += 1

    print("Ingrese su nombre:")

    nombre = input()

    print("Ingrese su edad: ")
    edad = int(input())


    print("Ingrese su estatura(ejem: 1.60):")
    estatura = float(input())

    print("Nombre:", nombre)
    print("________________")

    print("Edad:", edad)
    if(edad >= 18):
      print("Mayor de edad")
    else:
        if(edad > 18):
          print("Menor de edad")

    print("________________")

    print("Estatura:", estatura,"m")
    if(estatura >= 1.75):
        print("Usted es alt@")
    else:
        if(estatura >= 1.50 and estatura <= 1.74):
            print("Estatura media")
        else:
            if(estatura < 1.50):
                print("Baja estatura")

    if (vuelta == limite):
        break
    print("________________________________________")





