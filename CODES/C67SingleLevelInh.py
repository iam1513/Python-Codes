class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        # Call the constructor of the base class 'Vehicle'
        super().__init__(brand, model)
        self.fuel_type = fuel_type

# Create an instance of 'Car'
my_car = Car(brand="Toyota", model="Camry", fuel_type="Gasoline")

# Accessing attributes using the instance
print("Brand:", my_car.brand)
print("Model:", my_car.model)
print("Fuel Type:", my_car.fuel_type)