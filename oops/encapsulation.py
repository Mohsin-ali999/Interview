class Car:
    def __init__(self,speed,color):
        # Here the speed and color are protected
        self.__speed=speed
        self.__color=color

    def set_speed(self,value):
        self.__speed= value
    
    def get_speed(self):
        return self.__speed

    def set_color(self,value):
        self.__color= value
    
    def get_color(self):
        return self.__color
    

ford = Car(200,'White')
huyndai = Car(130,"Red")

print('The top speed of ford model is:',ford.get_speed())
print("The color of ford model is:",ford.get_color())
print('The top speed of ford model is:',huyndai.get_speed())
print("The color of ford model is:",huyndai.get_color())