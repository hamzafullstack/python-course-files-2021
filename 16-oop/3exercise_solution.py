class Laptop:
    def __init__(self, Brand, Name, Price):
        self.Brand = Brand
        self.Name = Name
        self.Price = Price
Laptop_one = Laptop('Hp', 'au114tx', 56000)
print(Laptop_one.Brand)