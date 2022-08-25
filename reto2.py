opcion=1
print("****** Menu ******")
print("1. multiplo")
print("2. raiz cuadrada")
print("0. salir")


while(opcion != 0):
    opcion=int(input("digite una opcion: "))
    if(opcion==1):
        print("sumando")
    elif(opcion == 2):
        print("restando")
    elif(opcion==0):
        break
    else:
        print("Digite una opcion valida")