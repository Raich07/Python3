pizza = input("¿Que tipo de pizza quieres? (vegetariana o no vegetariana)")
if(pizza=="vegetariana"):
    print("Ingredientes: Pimiento y tofu.")
    ingrediente = input("Elige uno de los anteriores")
    print("Tu pizza vegetariana tiene mozzarella, tomate y ", ingrediente)
elif(pizza=="no vegetariana"):
    print("Ingredientes: Peperoni, Jamón y Salmón")
    ingrediente2 = input("Elige uno de los anteriores")
    print("Tu pizza no vegetariana tiene mozzarella, tomate y ", ingrediente2)
else:
    print("No tenemos de eso")