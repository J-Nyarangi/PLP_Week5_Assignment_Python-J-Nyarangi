# Define a base class for a Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery Life: {self.battery_life} hours"

    def call(self, number):
        return f"Calling {number} from {self.model}..."

# Define a subclass for a GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu

    def specs(self):
        base_specs = super().specs()
        return f"{base_specs}, GPU: {self.gpu}"

    def game(self, game_name):
        return f"Playing {game_name} on {self.model} with {self.gpu}..."

# Create objects and test
phone = Smartphone("Apple", "iPhone 14", 128, 20)
print(phone.specs())
print(phone.call("123-456-7890"))

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, 30, "Adreno 730")
print(gaming_phone.specs())
print(gaming_phone.game("PUBG"))

### Activity 2: Polymorphism Challenge! 🎭
# Defining a base class for vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Define a Car class
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Define a Plane class
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Define a Boat class
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Test polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
