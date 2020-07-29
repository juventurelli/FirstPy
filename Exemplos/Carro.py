# class Carro():
#     estado = "novo"
#     def dirigir(self):
#         self.estado = "usado"

# porsche = Carro()
# porsche.dirigir()
# print(porsche.estado)

# ferrari = Carro()
# print(ferrari.estado)

# class Carro():

#     def __init__(self,estado):
#         self.estado = estado    

#     def dirigir(self):
#         self.estado = "usado"

# bmw = Carro("seminovo")
# print(bmw.estado)

## nome eh uma super classe
# class Nome():
    
#     def __init__(self):    
#         self.firstname = None
#         self.lastname = None

# class Pessoa():
    
#     def __init__(self):
#         self.nome = Nome()
#         self.estado = None    

# ju = Pessoa()
# ju.nome.firstname = "Ju"
# ju.nome.lastname = "Vnt"
# print("First name is " + ju.nome.firstname)
# print("Last name is {} ". format(ju.nome.lastname))

# class BankAccount:

#     def __init__ (self,name,balance = 0):
#         self.log("Account created "+ name)
#         self.name = name
#         self.balance = balance

#     def getBalance(self):
#         self.log("Balance checked at " + str(self.balance) + self.name)     
#         return self.balance

#     def deposit(self, amount):
#         self.balance += amount
#         self.log("New balance of "+ self.name + " is "  + str(self.balance))
        
#     def withdraw(self, amount):
#         self.balance -= amount
#         self.log("Whithdraw of "+ self.name + ": " + str(amount))

#     def log(self, message):
#         myLog = open("Log.txt", "a")
#         print(message, file = myLog)
#         myLog.close()

# myBank = BankAccount("Juju")           
# print(myBank.getBalance())
# myBank.deposit(20)
# print(myBank.getBalance())
# myBank.withdraw(100)
# print(myBank.getBalance())

# class Person:
#     def __init__(self,name,eyecolor,age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age

# class Name:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

# # def capitalizeName(name):                       ## muda o objeto
# #     name.firstname = name.firstname.upper()              
# #     name.lastname = name.lastname.upper()

# def capitalizeName(instring):                      ## nao muda o objeto
#       instring = instring.upper()  
#       print(instring) 


# myPerson = Person(Name("Ju", "Vent"), "brown", 33)
# capitalizeName(myPerson.name.firstname) 
# print(myPerson.name.firstname) 
# print(myPerson.name.lastname)

# class Artist:
#     def __init__(self, name, label):
#         self.name = name
#         self.label = label

# class Song:
#     def __init__(self, name, album, year, artist):
#         self.name = name
#         self.album = album
#         self.year = year
#         self.artist = artist

# #This function can actually be written in only a single line.
# #First, we declare the function:
# def get_song_string(a_song):
    
#     #Then, we create the string. Since we want to use quotation
#     #marks inside the string, we'll use apostrophes to create
#     #our string. 
#     #return '"' + a_song.name + '" - ' + a_song.artist.name + ' (' + str(a_song.year) + ')'

#     #We could also use our alternative string formatting syntax,
#     #which makes this even easier to read:
#     #
#     return '"{0}" - {1} ({2})'.format(a_song.name, a_song.artist.name, a_song.year)
        
# #Below are some lines of code that will test your function.
# #You can change the value of the variable(s) to test your
# #function with different inputs.
# #
# #If your function works correctly, this will originally
# #print: "You Belong With Me" -Taylor Swift (2008)
# new_artist = Artist("Taylor Swift", "Big Machine Records, LLC")
# new_song = Song("You Belong With Me", "Fearless", 2008, new_artist)
# print(get_song_string(new_song))


# class Person:
#     def __init__(self, name, eyecolor, age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age

# class Name:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

# myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
# myPerson2 = Person(Name("David", "Joyner"), "brown", 30)
# myPerson2.eyecolor = "blue"
# print("myPerson1's eyecolor: " + myPerson1.eyecolor)
# print("myPerson2's eyecolor: " + myPerson2.eyecolor)

# class Car:
#     def __init__(self,company,speed,color,year):
#         self.company = company
#         self.speed = speed
#         self.color = color
#         self.year = year
#     def get_speed(self):
#         print(self.speed)
#     def get_company(self):
#         print(self.company)
#     def get_color(self):
#         print(self.color)
#     def get_year(self):
#         print(self.year)

# class Trike(Car):
#     def __init__(self,company,speed,color,year):
#         self.company = company
#         self.speed = speed
#         self.color = color
#         self.year = year

# Car1 = Car("ABC",125,"RED",2019)
# Car2 = Car("XYZ",150,"BLUE",2020)
# Car3 = Car("LMN",200,"YELLOW",2020)
# Trike1 = Trike("GHJ",90,"Grey",2020)
# Trike2 = Trike("DFG",80,"Violet",2019)
# Trike1.get_speed()
# Trike1.get_company()
# Trike2.get_color()
# Trike2.get_year()

# class Car:
#     def __init__(self,company,speed,color,year):
#         self.company = company
#         self.speed = speed
#         self.color = color
#         self.year = year
#     def get_speed(self):
#         print(self.speed)
#     def get_company(self):
#         print(self.company)
        
# class Trike():
#     def __init__(self,company,speed,color,year):
#         self.company = company
#         self.speed = speed
#         self.color = color
#         self.year = year
#     def get_color(self):
#         print(self.color)
#     def get_year(self):
#         print(self.year)
        
# class Cycle(Car,Trike):
#     def __init__(self,company,speed,color,year):
#         self.company = company
#         self.speed = speed
#         self.color = color
#         self.year = year

# Car1 = Car("ABC",125,"RED",2019)
# Car2 = Car("XYZ",150,"BLUE",2020)
# Car3 = Car("LMN",200,"YELLOW",2020)
# Trike1 = Trike("GHJ",90,"Grey",2020)
# Trike2 = Trike("DFG",80,"Violet",2019)
# Cycle1 = Cycle("WER",30,"RED",2020)
# Cycle1.get_company()
# Cycle1.get_color()

# class Car:
#     def __init__(self,company,speed,color,year):
#         self.company = company
#         self.speed = speed
#         self.color = color
#         self.year = year
#     def get_speed(self):
#         print(self.speed)
#     def get_company(self):
#         print(self.company)
#     def get_color(self):
#         print(self.color)
#     def get_year(self):
#         print(self.year)
        
# class Trike(Car):
#     def __init__(self,company,speed,color,year):
#         self.company = company
#         self.speed = speed
#         self.color = color
#         self.year = year

# class Cycle(Trike):
#     def __init__(self,company,speed,color,year):
#         self.company = company
#         self.speed = speed
#         self.color = color
#         self.year = year
        
# Car1 = Car("ABC",125,"RED",2019)
# Car2 = Car("XYZ",150,"BLUE",2020)
# Car3 = Car("LMN",200,"YELLOW",2020)
# Trike1 = Trike("GHJ",90,"Grey",2020)
# Trike2 = Trike("DFG",80,"Violet",2019)
# Cycle1 = Cycle("WER",30,"RED",2020)
# Cycle1.get_company()
# Cycle1.get_color()

# class Animal:
#   def __init__(self, Animal):
#     print(Animal, 'is an animal.');

# class Mammal(Animal):
#   def __init__(self, mammalName):
#     super().__init__(mammalName)
#     print(mammalName, 'is a warm-blooded animal.')
    
    
# class NonWingedMammal(Mammal):
#   def __init__(self, NonWingedMammal):
#     print(NonWingedMammal, "can't fly.")
#     super().__init__(NonWingedMammal)

# class NonMarineMammal(Mammal):
#   def __init__(self, NonMarineMammal):
#     print(NonMarineMammal, "can't swim.")
#     super().__init__(NonMarineMammal)

# class Dog(NonMarineMammal, NonWingedMammal):
#   def __init__(self):
#     print('Dog has 4 legs.');
#     super().__init__('Dog')
    
# d = Dog()
# print('')
# bat = NonMarineMammal('Bat')

# class Bird:
    
#     def __init__(self):
#         print("Bird is ready")

#     def whoisThis(self):
#         print("Bird")

#     def swim(self):
#         print("Swim faster")

# class Penguin(Bird):

#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")

#     def whoisThis(self):
#         print("Penguin")

#     def run(self):
#         print("Run faster")

# bird = Penguin()
# bird.whoisThis()
# bird.run()
# bird.swim()

# class Computer:

#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Computer()
# c.sell()

# c.__maxprice = 1000  ## nao deixa mexer no preco
# c.sell()

# c.setMaxPrice(1000)
# c.sell()

# class Parrot:

#     def fly(self):
#         print("Parrot can fly")
    
#     def swim(self):
#         print("Parrot can't swim")

# class Penguin:
#     "class penguin" 
#     def fly(self):
#         print("Penguin can't fly")
    
#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# #instantiate objects
# blu = Parrot()
# peggy = Penguin()

# flying_test(blu)
# flying_test(peggy)

# print(Penguin.__doc__)

# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])



# class Triangle(Polygon):
#     def __init__(self):
#         super().__init__(self,3)

#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)


# triangulo = Polygon(3)
# print(triangulo.sides)
# triangulo.inputSides()
# triangulo.dispSides()

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#                                                   ## overload the print method
#     def __str__(self):                            ## controls how the object gets printed
#         return "({0},{1})".format(self.x,self.y)  ## definindo como o print vai funcionar

#     def __add__(self, other):
#             x = self.x + other.x
#             y = self.y + other.y
#             return Point(x, y)

# p1 = Point(1, 2)
# p2 = Point(2, 3)

# print(p1+p2)

my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))