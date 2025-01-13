from pathlib import Path
import json

path = Path('workwithfiles/numbers.json')

lectura  = int(json.loads(path.read_text()))

number = int(input("Por favor introduce un numero a guardar: "))

if lectura != number:

    number_json = json.dumps(int(number))
    path.write_text(number_json)
    print('Tu numero ha sido guardado, tu número es el: ' + number_json)
else:
    print(f"Your number already exists , you number is: {lectura}")

