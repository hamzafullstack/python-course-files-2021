# in this class we learn about
# encapsulation # apne data ko aur uske sath functionality perform krne wale methods etc
# Abstraction # sort etc
# some special name conventions # _name_ convention of private name # __name__ dunder method/magic
# name mangling # __name # not convention

class Phone:
    "phone is my class name"
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def Make_a_call(self,phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass

phone_one = Phone('ViVo', 'Y11', 24000)
print(phone_one.price)
# everything is Public in Python,, nothing Private
# _name =>> convention of private name (Not Rule)
# __name__ dunder/Magic/double underscore