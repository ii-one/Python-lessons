class Room(object):

    def __init__(self, number, max_seats):
        self.number = number
        self.max_seats = max_seats
        self.now_in_room = []

    def welcome(self, incoming):
        if len(self.now_in_room) >= self.max_seats:
            raise ValueError('Too many people')
        else:
            self.now_in_room.append(incoming)
            print('Welcome, {}'.format(incoming.name))


class Person(object):

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

class Speaker(Person):
    def __init__(self, name, topic):
        super().__init__("Mr. " + name)
        self.topic = topic


room_32 = Room('Room 32', 3)
room_27 = Room('Big room 27', 150)

student_1 = Student('Ivan', 1)
student_2 = Student('Sergey', 2)
student_3 = Student('Marina', 1)
student_4 = Student('Egor', 4)
speaker_1 = Speaker('Alexey','I like Python')

room_32.welcome(student_1)
room_32.welcome(speaker_1)
