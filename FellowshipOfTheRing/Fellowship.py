from Member import Member

class Fellowship():
    
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

    def fellowship(self):
        return(self.__name__)

  