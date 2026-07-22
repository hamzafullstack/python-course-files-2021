# rais error example
# not iplemented error
# abstracted method

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        raise NotImplementedError("You have to define this method in subclasses")

class Lion(Animal):
    def __init__(self,name,Roar):
        super().__init__(name)
        self.Roar = Roar

    def sound(self):
        return 'i dont know how to sound like Lion in Terminal '

class Tiger(Animal):
    def __init__(self,name,Roar):
        super().__init__(name)
        self.Roar = Roar

    def sound(self):
        return "Sorry i dont know how to sound like Tiger in Terminal "

lion_king = Lion('The Great Lion', 'king of Jungle')
print(lion_king.sound())