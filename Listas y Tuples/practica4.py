num_ganador = []
for i in range(6):
    num = int(input("Introduce el numro ganador: "))
    num_ganador.append(num)
    num_ganador.sort()
    print("Los numeros ganadores ordenados son: ", num_ganador)