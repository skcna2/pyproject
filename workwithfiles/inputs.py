people = input("how many people will be in yout dinner group?: ")
people = int(people)

if people > 8 :
    print('we dont have a table that size')
elif people <= 5:
    print('we will place you on a single table')    
else :
    print("we have a table for you")    



#while loops + imput
#while loop
promp = "write the toppings you want to add to the pizza,"
promp += "\nwrite quit to finish"
pizza_toppings = []

while pizza_toppings != 'quit':
   topping = input(promp)

   if topping != 'quit':
       pizza_toppings.append(topping)
       print(f'Topping {topping} added to the pizza')
   elif topping == 'quit':
     break

print(f'Tu pizza tiene todos los ingredientes: {pizza_toppings[:]}')