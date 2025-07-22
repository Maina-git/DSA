
class Car:     # is  key word to defint the class in python
     def __init__(self, make, model, year): #constructor method called automatically when you create a new object
 #self refers to a specific object being created 
 #the others are the parameters we pass when we create a car object 
         self.make = make
         self .model = model
         self.year = year
         self.odometer = 0

#methods
     def drive(self, miles):
         if miles > 0:
            self.odometer +=miles
            print(f"Driven {miles} miles. Total mileage is now {self}")
         else:
             print("Miles must be greater than 0.")

#methods
     def get_info(self):
         return f"{self.year} {self.make} {self.model}, Odometer:{self.odometer} miles"
  
 #example usage 
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_info())
my_car.drive(150)
print(my_car.get_info())













