class Car:
    def __init__(self, make, model, year):
        self.make = make      # e.g. 'Toyota'
        self.model = model    # e.g. 'Corolla'
        self.year = year      # e.g. 2020
        self.odometer = 0     # default value when car is new

    def drive(self, miles):
        if miles > 0:
            self.odometer += miles
            print(f"Driven {miles} miles. Total mileage is now {self.odometer}.")
        else:
            print("Miles must be greater than 0.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Odometer: {self.odometer} miles"

# Example usage
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_info())   # Output: 2020 Toyota Corolla, Odometer: 0 miles
my_car.drive(150)          # Output: Driven 150 miles...
print(my_car.get_info())   # Updated odometer info
