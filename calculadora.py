 # CALCULADORA 
print("--CALCULADORA--")
num1 = int(input("Ingrese un número: "))
operacion = (input("Operador: (+ - * /)"))
num2 = int(input("Ingrese un segundo número: "))

match operacion:
  case "+":
    resultado = num1 + num2
    print(f"El resultado de tu operación es: {resultado}")
  case "-":
    resultado = num1 - num2  
    print(f"El resultado de tu operación es: {resultado}")
  case "*":
    resultado = num1 * num2
    print(f"El resultado de tu operación es: {resultado}")
  case "/":
    if num2 == 0:
      print("Error: No se puede dividie entre 0.")
    else:
      resultado = num1 / num2
  case _:
    print("Operador ingresado incorrecto")  

