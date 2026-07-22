# Class variable
class Laptop:
    discount_percent = 10 # class variable
    def __init__(self, Brand, Name, Price):
        self.Brand = Brand
        self.Name = Name
        self.Price = Price

    def Apply_discount(self):
        off_price = (Laptop.discount_percent/100)*self.Price #aplyment
        return self.Price - off_price
Laptop_one = Laptop('Hp', 'au114tx', 56000)
print(Laptop_one.Apply_discount())