# 7class_variable_part2.py
# Class variable
class Laptop:
    discount_percent = 10 # class variable
    def __init__(self, Brand, Name, Price):
        self.Brand = Brand
        self.Name = Name
        self.Price = Price

    def Apply_discount(self):
        off_price = (self.discount_percent/100)*self.Price #self used for extra
        return self.Price - off_price
        
# agar sell khatam ho gyi discount ko khatam karna hai to simply......
#Laptop.discount_percent = 0
Laptop_one = Laptop('Hp', 'au114tx', 56000)
Laptop_one.discount_percent = 50
print(Laptop_one.__dict__)
print(Laptop_one.Apply_discount())