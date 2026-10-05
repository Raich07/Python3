fecha = input("¿Cual es tu fecha de nacimiento(ponlo en formato dd/mm/aaaa)?")
dia = fecha.split("/")[0]
mes = fecha.split("/")[1]
anio = fecha.split("/")[2]
print("Has nacido el día", dia, ", el mes ", mes, "y el año ", anio)