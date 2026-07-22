class Phone:
    "phone is my class name"
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0) # trick
        # if price > 0:
            #self.price = price
        #else:
            # self.price = 0
        self.complete_specification = f"{self.brand} {self.model_name} and price is {self.price}"

    def Make_a_call(self,phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass

phone_one = Phone('ViVo', 'Y11', 24000)
#print(phone_one.price)
print(phone_one.complete_specification)
# setter and getter,
# property etc left