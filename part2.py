class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        print("A vehicle has been created")

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight} kg")

    def honk(self):
        print("Generic honk sound.")

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        print("A car has been created")

    def honk(self):
        print("Beep beep!")

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, payload_capacity):
        super().__init__(make, model, year, weight)
        self.payload_capacity = payload_capacity
        print("A truck has been created")

    def honk(self):
        print("Honk honk!")

    def dump_load(self):
        print("Dumping payload...")

class Boat(Vehicle):
    def __init__(self, make, model, year, weight, boat_type):
        super().__init__(make, model, year, weight)
        self.boat_type = boat_type
        print("A boat has been created")

    def honk(self):
        print("Toot toot!")

    def drop_anchor(self):
        print("Dropping the anchor...")

# Example for Car
myCar = Car(make="Toyota", model="Camry", year=2023, weight=1500, num_doors=4)
myCar.display_info()
myCar.honk()

# Example for Truck
myTruck = Truck(make="Ford", model="F-150", year=2023, weight=2500, payload_capacity=5000)
myTruck.display_info()
myTruck.honk()
myTruck.dump_load()

# Example for Boat
myBoat = Boat(make="SeaCraft", model="Sailor", year=2023, weight=1500, boat_type="Sailboat")
myBoat.display_info()
myBoat.honk()
myBoat.drop_anchor()