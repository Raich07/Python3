numero = int(input("Dime un número entero"))
for contador in range(1, numero + 1, 2):
    for resta in range (contador, 0, -2):
        print(resta,end=" ")
    print() 