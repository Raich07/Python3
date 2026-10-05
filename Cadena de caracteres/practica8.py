precio = input("¿Cuanto era el precio del producto(dimelo con dos decimales)?")
euros = precio.split(",")[0]
centimos = precio.split(",")[1]
print("El producto vale ", euros ,"euros y", centimos, "centimos.")