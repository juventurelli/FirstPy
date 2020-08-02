
class Person():

    def __init__(self, nom):
        self.nom = nom
        print("{} created".format(self.nom))
    
    def name(self):
        return(self.nom)

    def toString(self):
        return(str(self.nom))    

    def fellowship(self):
        return()

class Wizzard(Person):
    def __init__(self,nom):
        super().__init__(nom)

class Human(Person):
    def __init__(self,nom):
        super().__init__(nom)

class Elf(Person):
    def __init__(self,nom):
        super().__init__(nom)

class Hobbit(Person):
    def __init__(self,nom):
        super().__init__(nom)

class Dwarf(Person):
    def __init__(self,nom):
        super().__init__(nom)      



from Member import Member
class Fellowship():
    
    def __init__(self, nom):
        self.nom= nom
        self.members = []
        print("Fellowship {} created".format(self.nom))

    def toString(self):
        return("Fellowship " + self.nom)    

    def signUp(self,nom):
        self.members.append(nom)
    
    def count(self):
         return len(self.members)

    def hasNoMembers(self):
        return len(self.members) == 0    

    def hasMembers(self):
        return len(self.members) != 0 

         


