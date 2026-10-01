barraPan = 3.49
panNoDia = round(barraPan * 0.4,2)
ventas = int(input("¿Cuantas barras de pan que no son del día se han vendido?"))
total = panNoDia * ventas
print(f"El precio normal es de  {barraPan}")
print(f"El precio con el descuento es de {panNoDia}")
print(f"El coste final total es de {total}")