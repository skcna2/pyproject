from pathlib import Path
import json

fav_number = input('Whats your favourite number: ')

formatted_num = json.dumps(int(fav_number))

path = Path("workwithfiles/numbers.json")

path.write_text(formatted_num)

print(f'Se ha añadido el número {fav_number} al fichero {path}')

#Leer el valor

path_leer = path.read_text() 

salida = json.loads(path_leer)

print(f'I know your favourite number is: {salida}')