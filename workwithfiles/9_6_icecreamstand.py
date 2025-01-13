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
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["Vainilla","menta","chocolate"]
    
    def display_icecream(self):
        for flavours in self.flavours:
            print(f"Tenemos sabor {flavours.title()}")
                  

    


heladeria = IceCreamStand("Pedro Jimenez","Española")
heladeria.display_icecream()