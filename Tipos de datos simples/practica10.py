pesoPayaso = 112
pesoMuneca = 75
numMuneca = int(input("¿Cuantas muñecas quieres?"))
numPayaso = int(input("¿Cuantos payasos quieres?"))
pesoTotal = (pesoPayaso*numPayaso + pesoMuneca*numMuneca)
print(f"Se han vendido {numMuneca} muñecas y {numPayaso} payasos")
print(f"El peso total es {pesoTotal}")