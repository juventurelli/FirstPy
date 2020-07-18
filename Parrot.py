class Parrot: 
 
    # class atribute
    species = "bird"

    #instance atribute
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def sing(self, song):
        return "{} is sings {}".format(self.name,song)
    
    def dance(self):
        return "{} is dancing".format(self.name)
        

# instantiate the Parrot class
blu = Parrot("Blue", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))

print(blu.sing("Happy"))
print(blu.dance())

class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")
        
        