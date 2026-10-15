edad = int(input("¿Cuantos años tienes?"))
if(edad<4):
    print("Puede entrar gratis")
elif(edad<18):
    print("Debe pagar 5€")
else:
    print("Debe pagar 10€")