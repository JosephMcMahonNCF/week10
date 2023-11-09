


class Car:
    def __init__(self, make, model, year, weight, num_doors):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors


    def display_info(self):
        print (f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight} kg\nNumber of Doors: {self.num_doors}")

    def honk(self):
        return print ("\033[3mhonk\033[0m")



# Creating an instance of the Car class
myBNW = Car(make="BMW", model="X5", year=2023, weight=1800, num_doors=4)

# Calling the display_info method
myBNW.display_info()

# Calling the honk method
myBNW.honk()





class Boat:
    def __init__(self, make, model, year, weight, boat_type):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.boat_type = boat_type

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight} kg\nBoat Type: {self.boat_type}")

    def honk(self):
        return print("HoonK")

class Truck:
    def __init__(self, make, model, year, weight, num_doors, payload_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors
        self.payload_capacity = payload_capacity

        print ("A truck has been created")

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight} kg\nNumber of Doors: {self.num_doors}\nPayload Capacity: {self.payload_capacity} kg")

    def honk(self):
        return print("HoNk!")

    def dump_load(self):
        return print("Dumping payload...")


class vehicle:
    def __init__(self, make, model, year, weight, num_doors):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors



if __name__ == "__main__":
    # Create instances of Vehicle Car
    car = Car("Toyota", "Corolla", 2021, 1275.0, 4)
    truck= Truck("Mac", "Street 750", 2019, 220.0, 4, 1001) #<--- but this now takes truck's constructor.

    # Display information of the car
    print("Car Info:")
    car.display_info()
    car.honk()
    print()


    # Display information of the motorcycle
    print("Truck Info:")
    truck.display_info()
    truck.honk()
    print()
