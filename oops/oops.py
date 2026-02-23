class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1 
        # self.total_car +=1
    
    def get_brand(self):
        return self.__brand + " !"
    
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fule_type(self):
        return "Petrol or Desiel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fule_type(self):
        return "ELECTRIC Charge"



# safari = Car("Tata", "Safari")
# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))


# safari.model = "Nexon"
# print(safari.model)
# safari.model = "Nexon"
# print(safari.full_name()) # we want to stop this change to happened 


# print(Car.general_description())

# print(safari.fule_type())
# print(my_tesla.fule_type())
# print(Car.total_car)
# print(my_tesla.__brand)
# print(my_tesla.get_brand())

# my_tesla.set_brand("BMW")
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.brand)
# print(my_tesla.full_name())
# my_car = Car("TATA", "Safari") # my_car is object

# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("TATA", "Safari")
# print(my_new_car.model)

class Battery:
    def bettey_info(self):
        return "This is battery info"

class Engine:
    def engine_info(self):
        return "This is Engine info"

class EV(Battery, Engine, Car):
    pass

my_newTesla = EV("Tesla", "Model M")

print(my_newTesla.engine_info())
print(my_newTesla.bettey_info())