class Member():
    def __init__(self,name):
        self.name = name    
        self.members = []
        
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