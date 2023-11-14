from part3 import Vehicle, Car, Truck, Boat
import random
class VehicleFactory:
    @staticmethod
    def create_vehicle():
        vehicle_type = random.choice(['Car', 'Truck', 'Boat'])
        make = random.choice(['Ford', 'Toyota', 'Honda'])
        model = 'ModelX'  # Simplified for this example
        year = random.randint(1990, 2022)
        weight = random.randint(1000, 3000)
        obj = None
        if vehicle_type == 'Car':
            obj = Car(make, model, year, weight, random.randint(2,5))
        elif vehicle_type == 'Truck':
            obj = Truck(make, model, year, weight, random.randint(1000, 2500))
        elif vehicle_type == 'Boat':
            obj = Boat(make, model, year, weight, random.randint(1000, 3500))
        print (obj)
        return obj






       ##Return the vehicle.

def process_vehicles(vehicles):
    for vehicle in vehicles:
        print(vehicle)
        vehicle.honk()

   #for each Car, Boat or other, print its contents and make it honk




# Testing
vehicle_list = [VehicleFactory.create_vehicle() for _ in range(5)] #<- what does this do? It makes a list is what it does

process_vehicles(vehicle_list)


