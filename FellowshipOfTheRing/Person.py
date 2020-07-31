class Person:

    def __init__(self, name):
        self.name = name
        print("I am {} ". format(self.name)) 

    def get_name(self):
        return(self.name)

    # def equals(self,name):
    #     return(self.name == name)

    # def toString(self):
    #     return(str(self.name))    


### Classe dos seres

class Wizzard(Person):
    def __init__(self,name):
        super().__init__(name)
        
class Human(Person):
    def __init__(self,name):
        super().__init__(name)

class Dwarf(Person):
    def __init__(self,name):
        super().__init__(name)

class Elf(Person):
    def __init__(self,name):
        super().__init__(name)

class Human(Person):
    def __init__(self,name):
        super().__init__(name)

class Hobbit(Person):
    def __init__(self,name):
        super().__init__(name)


###

class Fellowship:
    
    def __init__(self, name):
        self.members = 0
        self.
        print("Fellowship of {}".format(name))
    
    def count(self):
        return self.members

    def hasNoMembers(self):
        return self.members == 0    

    def hasMembers(self):
        return self.members != 0 

    def signUp(name):
