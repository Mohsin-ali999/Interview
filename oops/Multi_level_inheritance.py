# Multi-Level inheritance
class Grandfather:
    def __init__(self,grandfather):
        self.grandfather = grandfather

class Father(Grandfather):
    def __init__(self, fathername , grandfather):
        self.fathername = fathername
        # Initialize the Grandfather Class
        Grandfather.__init__(self,grandfather)

class Child(Father):
    def __init__(self,childname , fathername, grandfather):
        self.childname = childname
        # Initialize the Father Class
        Father.__init__(self,fathername, grandfather)

    def printname(self):
        print("Grand Father name:", self.grandfather)
        print("Father Name:", self.fathername)
        print("Child Name:", self.childname)

s1= Child('Mohsin Ali','Manzoor Ahmed', "Rehmatullah")
s1.printname()