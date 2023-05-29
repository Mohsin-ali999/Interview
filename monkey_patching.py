# # Monkey Patching

# class Test:
#     def __init__(self,x):
#         self.a =x
#     def get_data(self):
#         print("This is to get data from database")
#     def f1(self):
#         self.get_data()
#     def f2(self):
#         self.get_data()

# T1 = Test(5)
# # T1.f1()
# # T1.f2()

# def new_data(self):
#     print("This is to get data from excel")

# Test.get_data=new_data
# print("After monkey patching")

# T1.f1()
# T1.f2()

class Maths:
    def method1(a,b):
            return a+b
    
def method2(a,b):
        return a-b

Maths.method1 = method2
print('After monkey patching')
    
result = Maths.method1(3,5)

print(result)



