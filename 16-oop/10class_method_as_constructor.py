# class method as a constructor

class Person:
    count_variable = 0
    def __init__(self,first_name,last_name,age):
        Person.count_variable += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
# constructors:-
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
    
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
p4 = Person.from_string('Ameerhamza,Baloch,20')
print(p4.full_name())