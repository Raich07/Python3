invertir = int(input("¿Cuanto vas a invertir?"))
interes = float(input("¿Cuanto interes tienes?"))
años = int(input("¿Cuantos años?"))
cifra = 1

while cifra <= años:
    invertir = invertir * (1 + interes /100)
    print(invertir)
    cifra = cifra + 1