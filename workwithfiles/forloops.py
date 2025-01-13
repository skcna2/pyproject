cars= ["bmw", "audi", "toyota", "subaru"]
for car in cars:
    print(f"Este es uno de mis coches favoritos: {car.title()}")

print("\nEstos son mis todos los coches que tengo")


#Pizza Exercise

pizzas=["atun","margarita","hawaina"]
for pizza in pizzas:
    print(f"i like {pizza} pizza")
print("\ni love pizza")


#Numerical Exercise
values=[]
for value in range(1,21):
    print(f"añadido a la lista el valor: {value}")
    values.append(value)
print(values)

print(min(values))
print(max(values))
print(sum(values))
print("\n")
print(values[:3])
print(values[3:])

#coping a full list

pizzas=["atun","margarita","hawaina"]
friend_pizzas=pizzas[:]
print(pizzas)
print(friend_pizzas)




          


