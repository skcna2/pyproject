from pathlib import Path
import json

file_cats = Path("workwithfiles/cat.txt")
file_dogs = Path("workwithfiles/dog.txt")
try:
 read_cats = file_cats.read_text()
 print(read_cats)
except FileNotFoundError:
  pass #Except silencioso, pasa al siguente sin decir nada
  
try:
 read_dogs = file_dogs.read_text()
 print(read_dogs.count('r'))
except FileNotFoundError:
  print("No se encontró la ruta del fichero")






