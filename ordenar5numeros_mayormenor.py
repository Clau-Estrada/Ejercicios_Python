#Ordenar cinco números de mayor a menor. Primer intento.

print("Ingresa el primer número: ")
num1 = int(input())
print("Ingresa el segundo número: ")
num2 = int(input())
print("Ingresa el tercer número: ")
num3 = int(input())
print("Ingresa el cuarto número: ")
num4 = int(input())
print("Ingresa el quinto número: ")
num5 = int(input())

if(num1>num2 and num2>num3 and num3>num4 and num4>num5): 
    print("",num1," - ",num2," - ",num3," - ",num4," - ",num5)
elif(num1>num2 and num2>num3 and num3>num5 and num5>num4):
    print("",num1," - ",num2," - ",num3," - ",num5," - ",num4)
elif(num1>num2 and num2>num4 and num4>num3 and num3>num5):
    print("",num1," - ",num2," - ",num4," - ",num3," - ",num5)
elif(num1>num2 and num2>num4 and num4>num5 and num5>num3):
    print("",num1," - ",num2," - ",num4," - ",num5," - ",num3)
elif(num1>num2 and num2>num5 and num5>num3 and num3>num4):
    print("",num1," - ",num2," - ",num5," - ",num3," - ",num4)
elif(num1>num2 and num2>num5 and num5>num4 and num4>num3):
    print("",num1," - ",num2," - ",num5," - ",num4," - ",num3)
elif(num1>num3 and num3>num2 and num2>num4 and num4>num5):
    print("",num1," - ",num3," - ",num2," - ",num4," - ",num5)
elif(num1>num3 and num3>num2 and num2>num5 and num5>num4):
    print("",num1," - ",num3," - ",num2," - ",num5," - ",num4)
elif(num1>num3 and num3>num4 and num4>num2 and num2>num5):
    print("",num1," - ",num3," - ",num4," - ",num2," - ",num5)
elif(num1>num3 and num3>num4 and num4>num5 and num5>num2):
    print("",num1," - ",num3," - ",num4," - ",num5," - ",num2)
elif(num1>num3 and num3>num5 and num5>num2 and num2>num4):
    print("",num1," - ",num3," - ",num5," - ",num2," - ",num4)
elif(num1>num3 and num3>num5 and num5>num4 and num4>num2):
    print("",num1," - ",num3," - ",num5," - ",num4," - ",num2)
elif(num1>num4 and num4>num2 and num2>num3 and num3>num5):
    print("",num1," - ",num4," - ",num2," - ",num3," - ",num5)
elif(num1>num4 and num4>num2 and num2>num5 and num5>num3):
    print("",num1," - ",num4," - ",num2," - ",num5," - ",num3)
elif(num1>num4 and num4>num3 and num3>num2 and num2>num5):
    print("",num1," - ",num4," - ",num3," - ",num2," - ",num5)
elif(num1>num4 and num4>num3 and num3>num5 and num5>num2):
    print("",num1," - ",num4," - ",num3," - ",num5," - ",num2)
elif(num1>num4 and num4>num5 and num5>num2 and num2>num3):
    print("",num1," - ",num4," - ",num5," - ",num2," - ",num3)
elif(num1>num4 and num4>num5 and num5>num3 and num3>num2):
    print("",num1," - ",num4," - ",num5," - ",num3," - ",num2)
elif(num1>num5 and num5>num2 and num2>num3 and num3>num4):
    print("",num1," - ",num5," - ",num2," - ",num3," - ",num4)
elif(num1>num5 and num5>num2 and num2>num4 and num4>num3):
    print("",num1," - ",num5," - ",num2," - ",num4," - ",num3)
elif(num1>num5 and num5>num3 and num3>num2 and num2>num4):
    print("",num1," - ",num5," - ",num3," - ",num2," - ",num4)
elif(num1>num5 and num5>num3 and num3>num4 and num4>num2):
    print("",num1," - ",num5," - ",num3," - ",num4," - ",num2)
elif(num1>num5 and num5>num4 and num4>num2 and num2>num3):
    print("",num1," - ",num5," - ",num4," - ",num2," - ",num3)
elif(num1>num5 and num5>num4 and num4>num3 and num3>num2):
    print("",num1," - ",num5," - ",num4," - ",num3," - ",num2)
elif(num2>num1 and num1>num3 and num3>num4 and num4>num5):
    print("",num2," - ",num1," - ",num3," - ",num4," - ",num5)
elif(num2>num1 and num1>num3 and num3>num5 and num5>num4):
    print("",num2," - ",num1," - ",num3," - ",num5," - ",num4)
elif(num2>num1 and num1>num4 and num4>num3 and num3>num5):
    print("",num2," - ",num1," - ",num4," - ",num3," - ",num5)
elif(num2>num1 and num1>num4 and num4>num5 and num5>num3):
    print("",num2," - ",num1," - ",num4," - ",num5," - ",num3)
elif(num2>num1 and num1>num5 and num5>num3 and num3>num4):
    print("",num2," - ",num1," - ",num5," - ",num3," - ",num4)
elif(num2>num1 and num1>num5 and num5>num4 and num4>num3):
    print("",num2," - ",num1," - ",num5," - ",num4," - ",num3)
elif(num2>num3 and num3>num1 and num1>num4 and num4>num5):
    print("",num2," - ",num3," - ",num1," - ",num4," - ",num5)
elif(num2>num3 and num3>num1 and num1>num5 and num5>num4):
    print("",num2," - ",num3," - ",num1," - ",num5," - ",num4)
elif(num2>num3 and num3>num4 and num4>num1 and num1>num5):
    print("",num2," - ",num3," - ",num4," - ",num1," - ",num5)
elif(num2>num3 and num3>num4 and num4>num5 and num5>num1):
    print("",num2," - ",num3," - ",num4," - ",num5," - ",num1)
elif(num2>num3 and num3>num5 and num5>num1 and num1>num4):
    print("",num2," - ",num3," - ",num5," - ",num1," - ",num4)
elif(num2>num3 and num3>num5 and num5>num4 and num4>num1):
    print("",num2," - ",num3," - ",num5," - ",num4," - ",num1)
elif(num2>num4 and num4>num1 and num1>num3 and num3>num5):
    print("",num2," - ",num4," - ",num1," - ",num3," - ",num5)
elif(num2>num4 and num4>num1 and num1>num5 and num5>num3):
    print("",num2," - ",num4," - ",num1," - ",num5," - ",num3)
elif(num2>num4 and num4>num3 and num3>num1 and num1>num5):
    print("",num2," - ",num4," - ",num3," - ",num1," - ",num5)
elif(num2>num4 and num4>num3 and num3>num5 and num5>num1):
    print("",num2," - ",num4," - ",num3," - ",num5," - ",num1)
elif(num2>num4 and num4>num5 and num5>num1 and num1>num3):
    print("",num2," - ",num4," - ",num5," - ",num1," - ",num3)
elif(num2>num4 and num4>num5 and num5>num3 and num3>num1):
    print("",num2," - ",num4," - ",num5," - ",num3," - ",num1)
elif(num2>num5 and num5>num1 and num1>num3 and num3>num4):
    print("",num2," - ",num5," - ",num1," - ",num3," - ",num4)
elif(num2>num5 and num5>num1 and num1>num4 and num4>num3):
    print("",num2," - ",num5," - ",num1," - ",num4," - ",num3)
elif(num2>num5 and num5>num3 and num3>num1 and num1>num4):
    print("",num2," - ",num5," - ",num3," - ",num1," - ",num4)
elif(num2>num5 and num5>num3 and num3>num4 and num4>num1):
    print("",num2," - ",num5," - ",num3," - ",num4," - ",num1)
elif(num2>num5 and num5>num4 and num4>num1 and num1>num3):
    print("",num2," - ",num5," - ",num4," - ",num1," - ",num3)
elif(num2>num5 and num5>num4 and num4>num3 and num3>num1):
    print("",num2," - ",num5," - ",num4," - ",num3," - ",num1)
elif(num3>num1 and num1>num2 and num2>num4 and num4>num5):
    print("",num3," - ",num1," - ",num2," - ",num4," - ",num5)
elif(num3>num1 and num1>num2 and num2>num5 and num5>num4):
    print("",num3," - ",num1," - ",num2," - ",num5," - ",num4)
elif(num3>num1 and num1>num4 and num4>num2 and num2>num5):
    print("",num3," - ",num1," - ",num4," - ",num2," - ",num5)
elif(num3>num1 and num1>num4 and num4>num5 and num5>num2):
    print("",num3," - ",num1," - ",num4," - ",num5," - ",num2)
elif(num3>num1 and num1>num5 and num5>num2 and num2>num4):
    print("",num3," - ",num1," - ",num5," - ",num2," - ",num4)
elif(num3>num1 and num1>num5 and num5>num4 and num4>num2):
    print("",num3," - ",num1," - ",num5," - ",num4," - ",num2)
elif(num3>num2 and num2>num1 and num1>num4 and num4>num5):
    print("",num3," - ",num2," - ",num1," - ",num4," - ",num5)
elif(num3>num2 and num2>num1 and num1>num5 and num5>num4):
    print("",num3," - ",num2," - ",num1," - ",num5," - ",num4)
elif(num3>num2 and num2>num4 and num4>num1 and num1>num5):
    print("",num3," - ",num2," - ",num4," - ",num1," - ",num5)
elif(num3>num2 and num2>num4 and num4>num5 and num5>num1):
    print("",num3," - ",num2," - ",num4," - ",num5," - ",num1)
elif(num3>num2 and num2>num5 and num5>num1 and num1>num4):
    print("",num3," - ",num2," - ",num5," - ",num1," - ",num4)
elif(num3>num2 and num2>num5 and num5>num4 and num4>num1):
    print("",num3," - ",num2," - ",num5," - ",num4," - ",num1)
elif(num3>num4 and num4>num1 and num1>num2 and num2>num5):
    print("",num3," - ",num4," - ",num1," - ",num2," - ",num5)
elif(num3>num4 and num4>num1 and num1>num5 and num5>num2):
    print("",num3," - ",num4," - ",num1," - ",num5," - ",num2)
elif(num3>num4 and num4>num2 and num2>num1 and num1>num5):
    print("",num3," - ",num4," - ",num2," - ",num1," - ",num5)
elif(num3>num4 and num4>num2 and num2>num5 and num5>num1):
    print("",num3," - ",num4," - ",num2," - ",num5," - ",num1)
elif(num3>num4 and num4>num5 and num5>num1 and num1>num2):
    print("",num3," - ",num4," - ",num5," - ",num1," - ",num2)
elif(num3>num4 and num4>num5 and num5>num2 and num2>num1):
    print("",num3," - ",num4," - ",num5," - ",num2," - ",num1)
elif(num3>num5 and num5>num1 and num1>num2 and num2>num4):
    print("",num3," - ",num5," - ",num1," - ",num2," - ",num4)
elif(num3>num5 and num5>num1 and num1>num4 and num4>num2):
    print("",num3," - ",num5," - ",num1," - ",num4," - ",num2)
elif(num3>num5 and num5>num2 and num2>num1 and num1>num4):
    print("",num3," - ",num5," - ",num2," - ",num1," - ",num4)
elif(num3>num5 and num5>num2 and num2>num4 and num4>num1):
    print("",num3," - ",num5," - ",num2," - ",num4," - ",num1)
elif(num3>num5 and num5>num4 and num4>num1 and num1>num2):
    print("",num3," - ",num5," - ",num4," - ",num1," - ",num2)
elif(num3>num5 and num5>num4 and num4>num2 and num2>num1):
    print("",num3," - ",num5," - ",num4," - ",num2," - ",num1)
elif(num4>num1 and num1>num2 and num2>num3 and num3>num5):
    print("",num4," - ",num1," - ",num2," - ",num3," - ",num5)
elif(num4>num1 and num1>num2 and num2>num5 and num5>num3):
    print("",num4," - ",num1," - ",num2," - ",num5," - ",num3)
elif(num4>num1 and num1>num3 and num3>num2 and num2>num5):
    print("",num4," - ",num1," - ",num3," - ",num2," - ",num5)
elif(num4>num1 and num1>num3 and num3>num5 and num5>num2):
    print("",num4," - ",num1," - ",num3," - ",num5," - ",num2)
elif(num4>num1 and num1>num5 and num5>num2 and num2>num3):
    print("",num4," - ",num1," - ",num5," - ",num2," - ",num3)
elif(num4>num1 and num1>num5 and num5>num3 and num3>num2):
    print("",num4," - ",num1," - ",num5," - ",num3," - ",num2)
elif(num4>num2 and num2>num1 and num1>num3 and num3>num5):
    print("",num4," - ",num2," - ",num1," - ",num3," - ",num5)
elif(num4>num2 and num2>num1 and num1>num5 and num5>num3):
    print("",num4," - ",num2," - ",num1," - ",num5," - ",num3)
elif(num4>num2 and num2>num3 and num3>num1 and num1>num5):
    print("",num4," - ",num2," - ",num3," - ",num1," - ",num5)
elif(num4>num2 and num2>num3 and num3>num5 and num5>num1):
    print("",num4," - ",num2," - ",num3," - ",num5," - ",num1)
elif(num4>num2 and num2>num5 and num5>num1 and num1>num3):
    print("",num4," - ",num2," - ",num5," - ",num1," - ",num3)
elif(num4>num2 and num2>num5 and num5>num3 and num3>num1):
    print("",num4," - ",num2," - ",num5," - ",num3," - ",num1)
elif(num4>num3 and num3>num1 and num1>num2 and num2>num5):
    print("",num4," - ",num3," - ",num1," - ",num2," - ",num5)
elif(num4>num3 and num3>num1 and num1>num5 and num5>num2):
    print("",num4," - ",num3," - ",num1," - ",num5," - ",num2)
elif(num4>num3 and num3>num2 and num2>num1 and num1>num5):
    print("",num4," - ",num3," - ",num2," - ",num1," - ",num5)
elif(num4>num3 and num3>num2 and num2>num5 and num5>num1):
    print("",num4," - ",num3," - ",num2," - ",num5," - ",num1)
elif(num4>num3 and num3>num5 and num5>num1 and num1>num2):
    print("",num4," - ",num3," - ",num5," - ",num1," - ",num2)
elif(num4>num3 and num3>num5 and num5>num2 and num2>num1):
    print("",num4," - ",num3," - ",num5," - ",num2," - ",num1)
elif(num4>num5 and num5>num1 and num1>num2 and num2>num3):
    print("",num4," - ",num5," - ",num1," - ",num2," - ",num3)
elif(num4>num5 and num5>num1 and num1>num3 and num3>num2):
    print("",num4," - ",num5," - ",num1," - ",num3," - ",num2)
elif(num4>num5 and num5>num2 and num2>num1 and num1>num3):
    print("",num4," - ",num5," - ",num2," - ",num1," - ",num3)
elif(num4>num5 and num5>num2 and num2>num3 and num3>num1):
    print("",num4," - ",num5," - ",num2," - ",num3," - ",num1)
elif(num4>num5 and num5>num3 and num3>num1 and num1>num2):
    print("",num4," - ",num5," - ",num3," - ",num1," - ",num2)
elif(num4>num5 and num5>num3 and num3>num2 and num2>num1):
    print("",num4," - ",num5," - ",num3," - ",num2," - ",num1)
elif(num5>num1 and num1>num2 and num2>num3 and num3>num4):
    print("",num5," - ",num1," - ",num2," - ",num3," - ",num4)
elif(num5>num1 and num1>num2 and num2>num4 and num4>num3):
    print("",num5," - ",num1," - ",num2," - ",num4," - ",num3)
elif(num5>num1 and num1>num3 and num3>num2 and num2>num4):
    print("",num5," - ",num1," - ",num3," - ",num2," - ",num4)
elif(num5>num1 and num1>num3 and num3>num4 and num4>num2):
    print("",num5," - ",num1," - ",num3," - ",num4," - ",num2)
elif(num5>num1 and num1>num4 and num4>num2 and num2>num3):
    print("",num5," - ",num1," - ",num4," - ",num2," - ",num3)
elif(num5>num1 and num1>num4 and num4>num3 and num3>num2):
    print("",num5," - ",num1," - ",num4," - ",num3," - ",num2)
elif(num5>num2 and num2>num1 and num1>num3 and num3>num4):
    print("",num5," - ",num2," - ",num1," - ",num3," - ",num4)
elif(num5>num2 and num2>num1 and num1>num4 and num4>num3):
    print("",num5," - ",num2," - ",num1," - ",num4," - ",num3)
elif(num5>num2 and num2>num3 and num3>num1 and num1>num4):
    print("",num5," - ",num2," - ",num3," - ",num1," - ",num4)
elif(num5>num2 and num2>num3 and num3>num4 and num4>num1):
    print("",num5," - ",num2," - ",num3," - ",num4," - ",num1)
elif(num5>num2 and num2>num4 and num4>num1 and num1>num3):
    print("",num5," - ",num2," - ",num4," - ",num1," - ",num3)
elif(num5>num2 and num2>num4 and num4>num3 and num3>num1):
    print("",num5," - ",num2," - ",num4," - ",num3," - ",num1)
elif(num5>num3 and num3>num1 and num1>num2 and num2>num4):
    print("",num5," - ",num3," - ",num1," - ",num2," - ",num4)
elif(num5>num3 and num3>num1 and num1>num4 and num4>num2):
    print("",num5," - ",num3," - ",num1," - ",num4," - ",num2)
elif(num5>num3 and num3>num2 and num2>num1 and num1>num4):
    print("",num5," - ",num3," - ",num2," - ",num1," - ",num4)
elif(num5>num3 and num3>num2 and num2>num4 and num4>num1):
    print("",num5," - ",num3," - ",num2," - ",num4," - ",num1)
elif(num5>num3 and num3>num4 and num4>num1 and num1>num2):
    print("",num5," - ",num3," - ",num4," - ",num1," - ",num2)
elif(num5>num3 and num3>num4 and num4>num2 and num2>num1):
    print("",num5," - ",num3," - ",num4," - ",num2," - ",num1)
elif(num5>num4 and num4>num1 and num1>num2 and num2>num3):
    print("",num5," - ",num4," - ",num1," - ",num2," - ",num3)
elif(num5>num4 and num4>num1 and num1>num3 and num3>num2):
    print("",num5," - ",num4," - ",num1," - ",num3," - ",num2)
elif(num5>num4 and num4>num2 and num2>num1 and num1>num3):
    print("",num5," - ",num4," - ",num2," - ",num1," - ",num3)
elif(num5>num4 and num4>num2 and num2>num3 and num3>num1):
    print("",num5," - ",num4," - ",num2," - ",num3," - ",num1)
elif(num5>num4 and num4>num3 and num3>num1 and num1>num2):
    print("",num5," - ",num4," - ",num3," - ",num1," - ",num2)
elif(num5>num4 and num4>num3 and num3>num2 and num2>num1):
    print("",num5," - ",num4," - ",num3," - ",num2," - ",num1)
else:
    print("Un momento, ¡se ingresaron números iguales!")
