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

    def fellowship(self):
        return(self.__name__)

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