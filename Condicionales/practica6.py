nombre = input("Dime tu nombre")
sexo = input("Dime tu sexo(hombre/mujer)")
if (nombre < "M" and sexo == "mujer" or nombre < "N" and sexo == "hombre" ):
    print("Estás en el grupo A")

else:
    print("Estás en el grupo B")

