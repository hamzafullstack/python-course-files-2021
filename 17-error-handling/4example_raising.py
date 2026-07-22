#raise error example 2
class Mobile:
    def __init__(self,name):
        self.name = name

class Mobilestore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobiles):
        if isinstance(new_mobiles, Mobile):
            self.mobiles.append(new_mobiles)
        else:
            raise TypeError("New mobile should be object of mobile class")

phone = Mobile('samsung galaxy note8')
mobostore = Mobilestore()
mobostore.add_mobile(phone)
print(mobostore.mobiles)