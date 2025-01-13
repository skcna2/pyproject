class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 2
    

    def set_number_served(self,number):
        self.number_served = number
        return self.number_served
    
    def increment_number_served(self, increment):
        self.number_served += increment
        return self.number_served
    
    def increment_login_attemps(self,login_attempts):
        self.login_attempts = login_attempts + 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

 


restaurant= Restaurant("Casa paco","Española")
print(f"El restaurante {restaurant.restaurant_name.title()} ha servido a {restaurant.set_number_served(5)} clientes") 
restaurant.increment_number_served(10)
print(restaurant.number_served)
print(restaurant.increment_login_attemps(3))
print(type(restaurant.reset_login_attempts()))

    