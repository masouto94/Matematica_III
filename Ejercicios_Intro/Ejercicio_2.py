#Preguntar fecha de nacimiento y decir en qué estación nació (primavera, verano, otoño,invierno)
from datetime import datetime
from typing import Literal
def get_season(given_date: datetime) -> Literal["Otoño","Invierno","Primavera","Verano"]:
    if datetime(given_date.year,3,21) <= given_date <= datetime(given_date.year,6,21):
        return "Otoño"
    elif datetime(given_date.year,6,21) <= given_date <= datetime(given_date.year,9,21):
        return "Invierno"
    elif datetime(given_date.year,9,21) <= given_date <= datetime(given_date.year,12,21):
        return "Primavera"
    return "Verano"

birth_date = None

while not birth_date:
    birth_date = input("Ingrese la edad de nacimiento (YYYY/MM/DD)\n")
    try:
        parsed_date = datetime.strptime(birth_date, "%Y/%m/%d")
    except ValueError:
        birth_date = None

print(f"La fecha de nacimiento {birth_date} es en {get_season(parsed_date)}")