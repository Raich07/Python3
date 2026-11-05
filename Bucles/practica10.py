num = int(input("Dime un numero entero: "))
divi = 0
for i in range(1, num + 1):
    if num % i == 0:
        divi = divi + 1
if divi == 2:
        print("El numero ", num , "es un numero primo")
else:
        print("El numero ", num , "no es un numero primo")