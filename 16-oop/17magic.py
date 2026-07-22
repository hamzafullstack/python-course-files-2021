#special magic method // dunder method
# operator overloading,
#polymorphism :- method overriding
class Phone: #Base class / Parent class
    "phone is my class name"
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def phone_name(self):
        return f"{self.brand} {self.model_name}"
# str, repr

    def __str__(self):
        return f"{self.brand} {self.model_name}"

    def __repr__(self):
        return f"{self.brand} {self.model_name}"

# str... nicely formated string (normal programmers)
# repr... for developers can be able debug quickly

# operator overloading
# def __add__(self, other):
#     return self.price other.price

# polymorphism
""" kis chez ki aik se ziada forums hona """


