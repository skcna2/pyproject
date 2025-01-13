"""class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
       


    def describe_restaurant(self):
        print("El restaurante se llama " + self.restaurant_name.title()+ " y sirve comida " +self.cuisine_type.title())
    
    def open_restaurant(self):
        print("The restaurant is opened")

my_restaurant = Restaurant("Meson Pedro","tradicional")
print(f"Mi restaurante se llama {my_restaurant.restaurant_name}")
print(f"Se encargad e hacer cocina {my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant1= Restaurant("casa paco","mediterranea")
my_restaurant2= Restaurant("la cantina","mexicana")
my_restaurant3= Restaurant("el molar", "filipina")

my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()
"""
class User:

    def __init__(self,first_name,last_name,dni,fecha_nacimiento):
        self.firt_name = first_name
        self.last_name = last_name
        self.dni = dni
        self.fecha_nacimiento= fecha_nacimiento

    def describe_user (self):

        print(self.firt_name.title())
        print(self.last_name.title())
        print(self.dni)
        print(self.fecha_nacimiento)

    def greet_user(self):
        print(f"Bienvenido {self.firt_name.title()} {self.last_name.title()}")

usuario1 = User("juan","fernandez","49088443D","1988")
usuario2 = User("jose","sanchez","49345543D","1922")
usuario3 = User("juan","lopez","49088443D","1934")   

usuario1.describe_user()
usuario2.describe_user()
usuario3.describe_user()

usuario1.greet_user()
usuario2.greet_user()
usuario3.greet_user()

class Admin(User):
    def __init__(self,first_name,last_name,dni,fecha_nacimiento):
        super().__init__(first_name,last_name,dni,fecha_nacimiento)
        self.privileges = Privileges()
        
    


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"Estos son los privilegios: ")
        for priv in self.privileges:
            print(priv)



usuario2_admin = Admin("jose","sanchez","49345543D","1922")    
usuario2_admin.privileges.show_privileges()