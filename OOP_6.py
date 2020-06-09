"""Визначити ієрархію легкових автомобілів. Створити таксопарк.
   Порахувати вартість автопарку. Провести сортування автомобілів парку за витратами палива.
   Знайти автомобіль у компанії, що відповідає заданому діапазону швидкості автомобіля."""


class Main:
    def __init__(self, cars):
        self.cars = cars

    def sort_cars(self):
        for _ in self.cars:
            self.cars = sorted(all_cars, key=lambda i: i.fuel_consumption)

        print("List of all cars:")
        c = 1
        for j in self.cars:
            print(c, ")", j.name, sep="")
            c += 1

        print("Sorting a car by increasing fuel consumption: ")
        for k in self.cars:
            print(k.name, "(", k.fuel_consumption, "liters per 100 km)", end=", ")


class Mercedes:
    def __init__(self, name, max_speed, color, price, fuel_consumption):
        self.name = name
        self.max_speed = max_speed
        self.color = color
        self.price = price
        self.fuel_consumption = fuel_consumption


class Chevrolet(Mercedes):
    pass


class Reno(Mercedes):
    pass


class Mazda(Mercedes):
    pass


mercedes = Mercedes("Mercedes", 200, "black", "30 000 $", 5)

chevrolet = Chevrolet("Chevrolet", 180, "red", "20 000 $", 4)

reno = Reno("Reno", 160, "grey", "10 000 $", 3)

mazda = Mazda("Mazda", 140, "green", "6 000 $", 2)

all_cars = [mercedes, chevrolet, reno, mazda]

cars_all = Main(all_cars)
print(cars_all.sort_cars())

start_speed = int(input("Enter the initial vehicle speed: "))
finish_speed = int(input("Enter the final speed of the car: "))
user_speed = range(start_speed, finish_speed + 1)

for car in all_cars:
    if car.max_speed in user_speed:
        print("{} - ideal car for you!".format(car.name))
