#Contar cuántas veces aparece la letra "a" en el string almacenado en la variable "letras"

import re

letras ="aofnmgfoiajgmipoafjgmvaporgjmaeporgvmeñfvjkaeñvknmarvnampvma{rvkameñrvkmaevlkaekvamlvnalvkaerjvakpvna{eñrvnaerv"

ocurrencies_of_a = re.findall("a",letras)
print(f"'a' aparece {len(ocurrencies_of_a)} veces")