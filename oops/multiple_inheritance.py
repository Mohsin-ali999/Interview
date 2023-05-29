class Father:
    def fname(self):
        print("This is from father")

class mother(Father):
    def mname(self):
        print("This is from mother")


class child(mother):
    pass

obj = child()
obj.fname
obj.mname