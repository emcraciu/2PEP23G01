class Car:
    type_x = '4x4'
    def __init__(self):
        self._color = None

    @property
    def color(self):
        """I'm the 'x' property."""
        return f'{self._color} Returned'

    @color.setter
    def color(self, value):
        self._color = f'Metalic {value}'

    @color.deleter
    def color(self):
        del self._color


car = Car()
print(car.color)
car.color = 'yellow'
print(car.color)
car.type_x = '2x2'
print(car.type_x)

car.__setattr__('color', 'blue')
print(car.color)

car.color = 'black'
print(car.color)

#car.__delattr__('color')
del car.color
#print(car.color)

car.color = 'new color'
print(car.color)

