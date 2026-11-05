contraseñaOficial = "hola"
contraseña = input("Pon tu contraseña:")
while contraseñaOficial != contraseña:
    print("Esa no es tu contraseña, prueba otra vez")
    contraseña = input("Pon tu contraseña")
print("Contraseña correcta")        