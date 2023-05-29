# def my_decor(func):
#     def wrapper():
#         print("Hello")
#         func()
#         print("Bye")
#     return wrapper

# @my_decor
# def functions():
#     print("Hi")


# functions()


def my_decor(func):
    def wrap():
        print("Above from wrap fucntion")
        func()
    return wrap

@my_decor
def func():
    print("below from func")

func()



#Lambda function
greet = lambda name: print("Hey there", name)

greet("Mohsin")