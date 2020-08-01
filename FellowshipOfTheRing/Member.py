class Member():
    def __init__(self,name):
        super().__init__(name)
    
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
