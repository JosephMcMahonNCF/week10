import random

class Vehicle:
    def __init__(self, vehicle_type, make, model, year, weight):
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def honk(self):
        raise NotImplementedError("Subclasses must implement the honk method")

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - Type: {self.vehicle_type}, Weight: {self.weight}kg"

class Car(Vehicle):
    def honk(self):
        return "Beep beep!"

class Truck(Vehicle):
    def honk(self):
        return "Honk honk!"

class Boat(Vehicle):
    def __init__(self, vehicle_type, make, model, year, weight, draft):
        super().__init__(vehicle_type, make, model, year, weight)
        self.draft = draft

    def honk(self):
        return "Toot toot!"

class VehicleFactory:
    @staticmethod
    def create_vehicle():
        vehicle_type = random.choice(['Car', 'Truck', 'Boat'])
        make = random.choice(['Ford', 'Toyota', 'Honda'])
        model = 'ModelX'  # Simplified for this example
        year = random.randint(1990, 2022)
        weight = random.randint(1000, 3000)

        if vehicle_type == 'Car':
            return Car(vehicle_type, make, model, year, weight)
        elif vehicle_type == 'Truck':
            return Truck(vehicle_type, make, model, year, weight)
        elif vehicle_type == 'Boat':
            draft = random.randint(1, 10)
            return Boat(vehicle_type, make, model, year, weight, draft)

def process_vehicles(vehicles):
    for vehicle in vehicles:
        try:
            print(vehicle)
            print(vehicle.honk())
        except Exception as e:
            print(f"Error processing vehicle: {e}")

# Testing
vehicle_list = [VehicleFactory.create_vehicle() for _ in range(5)]
process_vehicles(vehicle_list)
