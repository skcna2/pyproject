age=True

while age == age:
    person_age=input('Para comprar ticket necesitamos saber tu edad, cuantos años tienes?: ')
    person_age = int(person_age)
    if person_age < 3:
        print("tu ticket no tienes coste, es gratis!!")
    elif person_age >= 3 and person_age <= 12:
        print("tu ticket son 10 dolares")
    elif person_age > 12:
        print("tu ticket vale 15 dolares")
    else:
        print("edad no valida")
    age=False