# Description: This file contains the code to create a list and print the elements of the list.
names=['julian','raul','luis','jose','julio']
print (names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

names[0]="pepeluis" #modificar un elemento de la lista
names.append('julian') #agregar un elemento a la lista
names.insert(0,"rodrigo") #agregar un elemento en una posicion especifica

print('this is a message for: ' + names[4].title())

del names [4] #eliminar un elemento de la lista
names.pop() #eliminar el ultimo elemento de la lista
names.pop(3) #eliminar un elemento de la lista

names.sort() #ordenar la lista de forma alfabetica
names.sort(reverse=True) #ordenar la lista de forma alfabetica inversa
print(sorted(names)) #ordenar la lista de forma temporal
reversed(names) #invertir la lista
names.resverse() #invertir la lista
len(names) #saber la longitud de la lista


print('this is a message for: ' + names[0].title())
print('this is a message for: ' + names[1].title())
print('this is a message for: ' + names[2].title())
print('this is a msesage for: ' + names[3].title())

