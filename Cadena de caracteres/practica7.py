correo = input("¿Cual es tu correo electronico?")
partes = correo.split("@")[0]
correoNuevo = partes + "@ceu.es"
print("Este es tu nuevo correo:", correoNuevo)