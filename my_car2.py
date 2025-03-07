# Example of importing an entire module and calling based on module & class name
import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_ev = car.ElectricCar('audi', 'r5', 2024)
print(my_ev.get_descriptive_name())