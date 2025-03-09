# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los
# clientes se guardarán en un diccionario en el que el
# key de cada cliente será su CUIT, y el valor
# será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente.
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2)
# Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes,
# (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
# • Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de
# datos.
# • Preguntar por el CUIT del cliente y eliminar sus datos de la base de datos.
# • Preguntar por el CUIT del cliente y mostrar sus datos.
# • Mostrar lista de todos los clientes de la base datos con su CUIT y nombre.
# • Mostrar la lista de clientes preferentes de la base de datos con su CUIT y nombre.
# • Terminar el programa.
import re

db = {}
class Client:
    def __init__(self, nombre:str, direccion:str, telefono:int, mail:str, preferente:bool):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.mail = mail
        self.preferente = preferente

def confirm(message:str) -> bool:
    if input(message).lower() in ["si", "sí"]:
        return True
    return False

def create_client(cuit:str, client_data: Client) -> None: 
    if db.get(cuit):
        print(f"Cliente:{db.get(cuit)}")
        if confirm(f"El cliente {cuit} ya existe. Sobreescribir? [Si/No]\n"):
            db[cuit] = client_data.__dict__
            print(f"Se sobreescribió {cuit}")
            return
        print("Se canceló la operacion")
        return
    db[cuit] = client_data.__dict__
    print(f"Se creó cliente {cuit} => {client_data.__dict__}")

def delete_client(cuit:str) -> None:
    if not db.get(cuit):
        print(f"El cuit {cuit} no existe como cliente")
        return
    if confirm(f"Se borrará cliente {cuit}. Continuar? [Si/No]\n"):
        del db[cuit]
        print(f"Se borro cliente {cuit}")
        return
    print("Se canceló la operacion")

def show_client(cuit:str) -> None:
    print(f"{cuit} => ",db.get(cuit,f"No se encontró al cliente {cuit}"))

def show_all():
    print(db)

def show_preferred_clients():
    print(
        dict(
            filter(lambda client: client[1].get("preferente"), db.items())
        )
    )

def parse_phone(phone_string:str) -> int:
    parsed_phone = re.sub(r"\D","",phone_string)
    return int(parsed_phone)

def validate_email(email_string:str) -> bool:
    pattern = r"\w+\@\w+\..*\w"
    if not re.match(pattern, email_string):
        return False
    return True

def parse_options() -> int:
    try:
        print("""Opciones disponibles:
              (1) Añadir cliente
              (2) Eliminar cliente
              (3) Mostrar cliente
              (4) Listar todos los clientes
              (5) Listar clientes preferentes
              (6) Terminar
              """)
        option = int(input("Ingrese la opcion deseada\n"))
        if 1 > option > 6:
            raise ValueError
    except ValueError:
        parse_options()
    return option
def main():
    option = None
    while option != 6:
        option = parse_options()

        if option == 1:
            cuit = input("Ingrese el cuit\n")
            client_name = input("Ingrese el nombre del cliente\n")
            client_address = input("Ingrese la direccion del cliente\n")
            client_phone = parse_phone(input("Ingrese el telefono del cliente\n"))
            client_email = input("Ingrese el email del cliente\n")
            while not validate_email(client_email):
                client_email = input("Ingrese un email válido\n")
            client_preferred = confirm("Ingrese si el cliente es preferente [Si/No]\n")
            client_data = Client(client_name,client_address,client_phone,client_email,client_preferred)
            create_client(cuit, client_data)
        
        elif option == 2:
            cuit = input("Ingrese el cuit\n")
            delete_client(cuit)
        
        elif option == 3:
            cuit = input("Ingrese el cuit\n")
            show_client(cuit)

        elif option == 4:
            show_all()

        elif option == 5:
            show_preferred_clients()

        elif option == 6:
            print("Programa terminado")

if __name__ == "__main__":
    main()