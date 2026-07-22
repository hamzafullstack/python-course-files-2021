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

class Flagship(Smart_phone):
    def __init__(self,brand,model_name, price, ram, storage, camera, front_camera):
        super().__init__(brand,model_name, price, ram, storage, camera)
        self.front_camera = front_camera

smartphone = Smart_phone('Oppo', 'A5', 20000, '4GB', '64GB', '20MP')
flagship_phone = Flagship('Samsung', 'Galaxy Note9', 100000, '8GB', '260GB', '30MP', '15MP')
############################################################
print(isinstance(smartphone, Smart_phone))
##########################################
print(issubclass(Smart_phone, Flagship))
