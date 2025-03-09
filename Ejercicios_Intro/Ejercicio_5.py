#Escribir un programa que pida al usuario dos números enteros (n y m) y muestre en pantalla: "La
#división entera entre n y m da un cociente c y un resto r" Donde n y m son los números
#introducidos por el usuario, y c y r son el cociente y el resto de la división entera
#respectivamente
from typing import Tuple

def integer_division(dividend: int, divisor:int) -> Tuple[int,int]:
    return (dividend//divisor, dividend % divisor)

dividend = None
divisor = None

while not isinstance(dividend, int) or not isinstance(divisor,int):
    try:
        dividend = int(input("Ingrese el dividendo\n"))
        divisor = int(input("Ingrese el divisor\n"))
        if divisor == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
        divisor = None    
    except ValueError:
        print("El divisor y el dividendo deben enteros")
        dividend = None
        divisor = None
        
quotient,remainder = integer_division(dividend,divisor)
print(f"El resultado de la division entera de {dividend} por {divisor} es => cociente {quotient} y resto {remainder}")