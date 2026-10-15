renta = int(input("¿Cuanto declaras en la renta?"))
if(renta<10000):
    print("Le corresponde un 5%")
elif(renta<20000):
    print("Le corresponde un 15%")
elif(renta<35000):
    print("Le corresponde un 20%")
elif(renta<60000):
    print("Le corresponde un 30%")
else:
    print("Le corresponde un 45%")
