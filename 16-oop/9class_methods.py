#  class methods
# difference between class methods and instance methods
# NOTE:- hum class methods buhat kam use karte hain
# kiyun ke yeh ziada usefull nahi hote hain

class Person:
    count_variable = 0
    def __init__(self,first_name,last_name,age):
        Person.count_variable += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def count_instances(cls):
        return f" You have created {cls.count_variable} instance of {cls.__name__} class "

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = Person('nawaz', 'baloch', 13)
p2 = Person('Hamza', 'baloch', 20)
p3 = Person('Murad', 'baloch', 20)
print(Person.count_instances())