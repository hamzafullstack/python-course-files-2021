class Laptop:
    def __init__(self, Brand, Name, Price):
        self.Brand = Brand
        self.Name = Name
        self.Price = Price

    def Apply_discount(self, num): #method
        off_price = (num/100)*self.Price #for discount
        return self.Price - off_price
Laptop_one = Laptop('Hp', 'au114tx', 56000)
print(Laptop_one.Apply_discount(10)) #applying method