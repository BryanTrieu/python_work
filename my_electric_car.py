from car import ElectricCar

my_ev = ElectricCar('Audi', 'R5', 2024)

print(my_ev.get_descriptive_name())
my_ev.battery.describe_battery()
my_ev.battery.get_range()