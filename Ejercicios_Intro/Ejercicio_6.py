#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
from getpass import getpass

password = getpass("Ingrese una contraseña\n")

login = None
while login != password:
    login = input("Ingrese la contraseña\n")