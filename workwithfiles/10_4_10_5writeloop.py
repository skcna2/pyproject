from pathlib import Path
 #
path =  Path ("workwithfiles/guest.txt")
nombres = ''

nombre= ''
while nombre != 'q':

 nombre = input("Introduce tu nombre y pulsa enter para ir añadiendo varios,q para terminar: ")
 
 if nombre != 'q':
     
  nombres += nombre + "\n"

 elif nombre == 'q':
        
        break
   

path.write_text(nombres.title())

print(path.read_text())

    