# Create instances of Car and Plane
car = Car("Toyota", "Corolla", 2020, "Gasoline")
plane = Plane("Boeing", "747", 2015, "Delta Airlines")

# List of vehicles
vehicles = [car, plane]

# Demonstrate polymorphism
for vehicle in vehicles:
    vehicle.move()
