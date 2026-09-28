invertir = int(input("¿Cuanto quieres invertir?"))
interes = int(input("¿Cuanto interes tienes?"))
años = int(input("¿Cuanto años vas a tenerlo?"))
capital = invertir * (1+(interes/100)) ** años
print("Tu capital sería de: ",capital)