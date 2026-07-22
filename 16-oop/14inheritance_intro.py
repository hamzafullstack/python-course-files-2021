class Phone: #Base class / Parent class
    "phone is my class name"
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def Make_a_call(self,phone_number):
        print(f"calling {phone_number}")
#######################################################################
class Smart_phone(Phone): #Diverd / child class / inheritance
    def __init__(self,brand,model_name, price, ram, storage, camera):
        super().__init__(brand,model_name, price)
        self.ram = ram
        self.storage = storage
        self.camera = camera


phone_one = Phone('nokia', '1100', 1000)
smartphone = Smart_phone('vivo', 'Y11', 2400, '4GB', '64 GB', '38 Mp')
print(phone_one.full_name())
print(smartphone.full_name())