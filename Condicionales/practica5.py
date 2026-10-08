edad = int(input("¿Cuantos años tienes?"))
ingreso = int(input("¿Cuanto ingresas mensualmente?"))
if(edad>16 and ingreso>=1000):
    print("Tienes que tributar") 
else:
    print("No tienes que tributar")