# instance method

# instance or object aik hi baat hai
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
# p1 is object(instance)
p1 = Person('Hamza', 'Baloch', 20)
p2 = Person('Hamza', 'Bugti', 20)
# print(p2.full_name())


#in actual aisa ho raha hota hai
# Person.full_name(p2) # but mostly log aisa likhna pasnad nahin karte
# sub ko shortcut ki parhi hoti hai

l = [1,2,3,4]
# list.clear(l)
#list will be clear we called clear method here
"""buhat si python developers nahi jante hum instance ko aise be use karte h"""
# list.append(l,5)
