# Single inheritance
class parent:
    def func(self):
        print("This is from parent class")

class child(parent):
    def func1(self):
        print("This is from child class")

obj= child()
obj.func()
obj.func1()

