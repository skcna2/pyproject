#a simple dictionary
alien_on= {'name': 'alien', 'points': 5, 'color': 'rojo'}
print(alien_on['name'])
print(alien_on['points'])

del alien_on['name']

alien_on['name']= 'alienado'
alien_on['x_position'] = 0
print(alien_on)

#uso del metodo get()
valor_input = input("introduce el valor: ")
valor_out = alien_on.get(valor_input,'we dont have the ' + valor_input + ' of the alien')
print(valor_out)

for id,valor in alien_on.items():
    print(id,valor)

for id in alien_on.keys():
    print(f"{alien_on[id]}")

