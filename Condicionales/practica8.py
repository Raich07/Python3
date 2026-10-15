puntos = float(input("¿Cuantos puntos has tenido?"))
dinero = 2400 * puntos
if(puntos == 0.0):
    print(f"Usted tiene un nivel INACEPTABLE y recibirá", dinero , "€")
elif(puntos == 0.4):
    print(f"Usted tiene un nivel ACEPTABLE y recibirá", dinero , "€")
elif(puntos >= 0.6):
    print(f"Usted tiene un nivel MERITORIO y recibirá", dinero , "€")