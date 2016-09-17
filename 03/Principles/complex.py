class Wheel(object):
    def __init__(self,diameter):
        self.diameter = diameter


class Car(object):
    def __init__(self, name, *wheels):
        self.name = name
        self.wheels = wheels

    def info(self):
        print('I have {} wheels'.format(
            len(self.wheels))
        )


class Truck(Car):
    def __init__(self, name, wheels_number, wheel_diameter):
        self.name = name
        self.wheels = []
        for i in range(wheels_number):
            wheel = Wheel(wheel_diameter)
            self.wheels.append(wheel)
        print('Wheels created')



wheels = []
for i in range(4):
    wheel = Wheel(13)
    wheels.append(wheel)

car = Car('BMW', *wheels)
car.info()

truck = Truck('Kamaz', 8, 29)
truck.info()
