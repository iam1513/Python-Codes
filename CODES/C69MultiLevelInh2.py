class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, num_doors):
        # Call the constructor of the base class 'Vehicle'
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.num_doors = num_doors

class SportsCar(Car):
    def __init__(self, brand, model, fuel_type, num_doors, top_speed):
        # Call the constructor of the base class 'Car'
        super().__init__(brand, model, fuel_type, num_doors)
        self.top_speed = top_speed

    def drive_fast(self):
        print(f"{self.brand} {self.model} is driving at {self.top_speed} mph. Hold on tight!")

# Create an instance of 'SportsCar'
my_sports_car = SportsCar(brand="Ferrari", model="488 GTB", fuel_type="Gasoline", num_doors=2, top_speed=205)

# Accessing inherited attributes
print("Brand:", my_sports_car.brand)
print("Model:", my_sports_car.model)

# Accessing attributes from the 'Car' class
print("Fuel Type:", my_sports_car.fuel_type)
print("Number of Doors:", my_sports_car.num_doors)

# Accessing attributes from the 'SportsCar' class
print("Top Speed:", my_sports_car.top_speed)

# Call the method introduced in the 'SportsCar' class
my_sports_car.drive_fast()
