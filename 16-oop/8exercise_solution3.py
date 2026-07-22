# OOP exercise solution
class Person:
    count_variable = 0
    def __init__(self,first_name,last_name,age):
        Person.count_variable += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('nawaz', 'baloch', 13)
p2 = Person('Hamza', 'baloch', 20)
p3 = Person('Murad', 'baloch', 20)
print(Person.count_variable)