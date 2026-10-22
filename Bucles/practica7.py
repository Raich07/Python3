numero1 = 1
numero2 = 1
while(numero1 <= 10):
    print (numero1 ,"x" ,numero2, "=", numero1 * numero2)
    numero2 = numero2 + 1
    if(numero2 == 11):
        numero2 = 1
        numero1 = numero1 + 1
        print("--------------")

    #for i in range(1,11):
        #for j in range(1,11):
            #print(i*j)
        #print(------------)