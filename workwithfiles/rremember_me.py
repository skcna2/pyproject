from pathlib import Path
import json



path = Path('workwithfiles/username.json')

def save_user():

 user_info={}
 username= input('Introduce el nombre del usuario: ')
 name = input('Intrduce tu nombre: ')
 apellido= input('introduce tu apellido: ')
 user_info['username'] = username
 user_info['name'] = name
 user_info['apellido'] = apellido

 print(user_info)
 
 
 contents = json.dumps(user_info)
 path.write_text(contents)

 print(f"we Will remember your when you come back {username}!")


def greetings():

    path_r = path.read_text()
    read_json = json.loads(path_r)
    print(f"Bienvenido de vuelta {read_json}")




    




save_user()
greetings()

