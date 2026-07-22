# Multiple inheritance..
# most of python developer avoid to use multiple inheritance

class A:
    def class_a_method(self):
        return "I'm just class A method"
    
    def Hello(self):
        return 'Hello from class A'

class B:
    def class_b_method(self):
        return "I'm just class B method"
    
    def Hello(self):
        return 'Hello from class B'

class C(A,B):
    pass

instance_c = C()
#print(instance_c.class_a_method())
#print(instance_c.class_b_method())
print(instance_c.Hello())