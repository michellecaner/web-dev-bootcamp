"""Python refresher course - Function Arguments & Parameters Section"""

def add(x, y): # x and y are the parameters 
    result = x + y
    print(result)

add(5, 3) # 5 and 3 are the arguments that provide value to the parameters




def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Gina") # must have argument when asking for a parameter or will break



def say_howdy(name, surname):
    print(f"Howdy, {name} {surname}!")

say_howdy("Justin", "Case") # positional arugments




def say_hola(name, surname):
    print(f"Hola, {name} {surname}!")

say_hola(name="Anita", surname="Cookie")  # keyword or named arguments which allow us to be super helpful



def user_name():
    print("Rolf")
    
user_name()



def greeting(name):
    print(f"Hello, {name}, how are you?")
    
greeting(name="Michelle")