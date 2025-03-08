#Pedirle la edad al usuario y responder si es divisible por 3

def es_divisible(edad:int, numero:int) -> None:
    if edad % numero == 0:
        print(f"La edad {edad} es divisible por {numero}")
        return
    print(f"La edad {edad} no es divisible por {numero}")

edad_usuario = None
while not edad_usuario: 
    try:
        edad_usuario = int(input("Ingrese la edad del usuario\n"))
    except ValueError:
        edad_usuario = None
es_divisible(int(edad_usuario),3)
