
class Person():

    def __init__(self, name):
        self.name = name
        print("{} created".format(self.name))
    
    def get_name(self):
        return(self.name)

    # def equals(self,name):
    #     return(self.name == name)

    # def toString(self):
    #     return(str(self.name))    

    def fellowship(self):
        return()

class Wizzard(Person):
    def __init__(self,name):
        super().__init__(name)

class Human(Person):
    def __init__(self,name):
        super().__init__(name)

class Elf(Person):
    def __init__(self,name):
        super().__init__(name)

class Hobbit(Person):
    def __init__(self,name):
        super().__init__(name)

class Dwarf(Person):
    def __init__(self,name):
        super().__init__(name)      



class Fellowship(Person):
    
    def __init__(self, name):
        self.name= name
        self.members = []
        print("Fellowship {} created".format(self.name))

    def signUp(self,name):
        self.members.append(name)
    
    def count(self):
         return len(self.members)

    def hasNoMembers(self):
        return len(self.members) == 0    

    def hasMembers(self):
        return len(self.members) != 0 

    def member(self, number):
        if len(self.members)>0:
            return(self.members[number-1])
        else:
            return None    

    def lastMember(self):    
        if len(self.members)>0:
            return(self.members[len(self.members)])
        else:
            return None     


