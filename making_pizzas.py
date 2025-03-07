#examples of different types of formatting for importing and using alias for modules and functions
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza as mp

mp(12, 'pepperoni')
mp(8, 'mushrooms', 'green peppers', 'extra cheese')

import pizza as p

p.make_pizza(16, 'sausage')
p.make_pizza(10, 'mushrooms')