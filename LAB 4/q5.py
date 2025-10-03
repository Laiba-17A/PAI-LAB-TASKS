from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self.__rental_price = rental_price
        self.__available = True

    def check_availability(self):
        if self.__available:
            print("is available for rent.")
        else:
            print( "is not available for rent.")
        return self.__available

    def rent_vehicle(self):
        if self.__available:
            self.__available = False
            print(self.make, self.model, "has been rented.")
        else:
            print(self.make, self.model, "is not available for rent.")

    def return_vehicle(self):
        self.__available = True
        print(self.make, self.model, "has been returned.")

    def cal_rental_cost(self, days):
        return self.__rental_price * days

    @abstractmethod
    def print_details(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def print_details(self):
        print("Car - Make:", self.make, ", Model:", self.model)

class SUV(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)
     
    def print_details(self):
        print("SUV - Make:", self.make, ", Model:", self.model)

class Truck(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)

    def print_details(self):
        print("Truck - Make:", self.make, ", Model:", self.model)

class customer:
    def __init__(self, name, contact):
        self.name = name
        self.__contact = contact
        self.rented_vehicles = []

    def add_rental(self, res):
        self.rented_vehicles.append(res)

    def printhistory(self):
        print()
        print("Rental History for", self.name)
        if not self.rented_vehicles:
            print("No rentals yet.")
        for res in self.rented_vehicles:
            res.print_reservation()

class reservation:
    def __init__(self, customer, vehicle, days):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days
        self.total_cost = vehicle.cal_rental_cost(days)

        if vehicle.check_availability():
            vehicle.rent_vehicle()
            customer.add_rental(self)
        else:
            print(vehicle.make, vehicle.model, "is already rented. Reservation failed.")

    def print_reservation(self):
        print()
        print(" Reservation Details")
        print("Customer Name:", self.customer.name)
        print("Vehicle:", self.vehicle.make, self.vehicle.model)
        print("Days Rented:", self.days)
        print("Total Cost: $", self.total_cost)
        print("Vehicle Available:", self.vehicle.check_availability())
        self.vehicle.print_details()

#main
car1 = Car("Toyota", "Corolla", 40)
suv1 = SUV("Honda", "CR-V", 60)
truck1 = Truck("Ford", "F-150", 90)

cust1 = customer("Laiba", "laiba@example.com")

res1 = reservation(cust1, car1, 3)
res2 = reservation(cust1, suv1, 5)
res3 = reservation(cust1, suv1, 2)

car1.print_details
res1.print_reservation()

suv1.return_vehicle()
res4 = reservation(cust1, suv1, 2)
cust1.printhistory()

