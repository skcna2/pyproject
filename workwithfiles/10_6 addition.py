

while True:

    number1 = input("Escribe 1 numero: ")
    number2 = input("Escribe un segundo numero: ")

    try:
     total = int(number1) + int(number2)
    except ValueError:
     print("NO puedes introducir letras, por favor introdcuza un número")    
    else:
      print(f"El total de los dos números es {total}")
      break
   