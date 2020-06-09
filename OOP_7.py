"""
List, Масив із початковою кількістю елементів 15 та збільшенням кількості елементів на 30%
4.	Створити клас, що описує типізовану колекцію (типом колекції є узагальнений клас з лабораторної роботи №6),
що реалізує заданий варіантом інтерфейс (п.2) та має задану внутрішню структуру (п.3).
Реалізувати всі методи інтерфейсу, а також створити не менше ніж 3 конструктори
(1 – порожній, 2 – в який передається 1 об’єкт узагальненого класу, 3 – в який передається стандартна колекція об’єктів)
Всі початкові дані задаються у виконавчому методі.
Код повинен відповідати стандартам JCC та бути детально задокументований.
"""


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


class MyArray:
    collection = [' '] * 15

    def main_func(self):
        if len(self.collection) > 15:
            to_extend = [' '] * int(len(self.collection) * 0.3)
            self.collection.extend(to_extend)

    @staticmethod
    def check_type(a):
        if type(a) is list or type(a) is set or type(a) is tuple or type(a) is dict is False:
            return True

    def collection_append(self, a):
        if MyArray.check_type(a):
            to_append = [a]
            self.collection = self.collection + to_append
            self.main_func()
            return self.collection
        else:
            print("Error!")

    def collection_remove(self, index):
        if type(index) is int is True:
            self.collection[index] = ''
        else:
            print('Error!')

    def collection_pop(self, index):
        if type(index) is int is True:
            self.collection[index] = ''
            to_pop = self.collection[index]
            return to_pop
        else:
            print('Error!')

    def collection_clear(self):
        for i in range(len(self.collection)):
            self.collection[i] = ''

    def collection_count(self, string):
        amount = 0
        for i in range(len(self.collection)):
            if str(string) == self.collection[i]:
                amount += 1
        if amount != 0:
            return amount
        else:
            return print('Error!')

    def collection_copy(self):
        copied = self.collection
        return copied

    def collection_reverse(self):
        temp = [' ']*len(self.collection)
        for i in range(len(self.collection)):
            temp[(len(self.collection)-1) - i] = self.collection[i]
        return temp

    def __init__(self, lst):
        for i in range(len(lst)):
            self.collection[i] = lst[i]
            self.main_func()


my_arr = MyArray(all_cars)
arr = MyArray([1, 2, 3])
print(arr.collection_append([23, 44, 75]))
print(arr.collection_reverse())
print(arr.collection_copy())
