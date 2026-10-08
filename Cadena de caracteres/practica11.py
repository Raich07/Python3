producto = input("Nombre del producto: ")
precio = float(input("Precio: "))
unidades = int(input("Unidades: "))

total = precio * unidades

print(f"{producto}: {precio:9.2f}€  {unidades:3d} unidades   total:{total:11.2f}€")