frase = input("Dime una frase: ")
letra = input("Dime una letra: ")
caracter = 0
for i in frase:
    if i == letra:
        caracter = caracter + 1
print(f"La  letra {letra} se repite {caracter} veces.")


