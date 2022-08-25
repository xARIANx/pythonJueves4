''''
numero = 5

while(numero < 10):
    print("Estoy adentro del acuerdo")
    numero+=1
else:
    print("adiossssss")
    
print("Estoy por fuera del acuerdo")
'''

opcion=1
print("****** Menu ******")
print("1. sumar")
print("2. restar")
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