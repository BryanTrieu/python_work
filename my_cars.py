from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_ev = EC('audi', 'r5', 2024)
print(my_ev.get_descriptive_name())