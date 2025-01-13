#ips= []
#user_in=""

#while user_in != "done":
 #    user_in= input("IP addressor type done to exit: ")
  #   if user_in != "done":
 #         ips.append(user_in)
#print (f"Your IPs are: {ips}")          


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

