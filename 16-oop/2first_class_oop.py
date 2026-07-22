# Objectives
# what is class :- class is a blueprint
# how to create a class
# what is init method :- init method is also called constructor
# what are arributes instance variables
# how to create our objects


# create first class (first later of class should be capital) (convension)
class Person:
    """ Our first class """
    def __init__(self, first_name, last_name, age):
        # instance variables
        """ init method \\ Constructor get called """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
p1 = Person('Hamza', 'Baloch', 20)
p2 = Person('muzammil', 'Bugti', 19)
p3 = Person('Abdul Sattar', 'Bugti', 20)
print(p1.first_name)
print(p2.first_name)
print(p3.first_name)
# NOTE:- self is a instance variable and we can write anything there instead of self
# NOTE:- according to MICROSOFT we should write self.. because of its an convension.. but not a rule