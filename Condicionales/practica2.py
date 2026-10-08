contraseña = "hola"
contraseñaPregu = str(input("¿Cual es tu contraseña?"))
contraseñaMin = contraseñaPregu.lower()
if (contraseña == contraseñaMin):
    print("Contraseña correcta")
else:
    print("No es la contraseña correcta")
