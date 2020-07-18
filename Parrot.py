""" class Parrot: 
 
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
        
class Peguin(Bird):

    def __init__(self):
        super().__init__()
        print("Peguin is ready")
    
    def whoisThis(self):   # child class modifies the behavior of the parent class
        print("Peguin")

    def run(self):         # child class extends the behavior of the parent class
        print("Run faster")

peggy = Peguin() 
peggy.whoisThis()
peggy.swim()        
peggy.run()        

 """

class Parrot():
    def fly(self):
        print("Parrot can fly")

    def fly(self):
        print("Parrot can't fly")
        
class Peguin():
    def fly(self):
        print("Peguin can't fly")

    def fly(self):
        print("Parrot can fly")


def flying_test(bird):
    bird.fly()