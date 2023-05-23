#### Importing Multiple Classes from a Module ####

# from car import Car, ElectricCar
# from car import Car
# from electric_car import ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())


#### Importing an Entire Module ####

import car
import electric_car

"""
This approach is simple and results in code that is easy
to read. Because every call that creates an instance of a class includes the
module name, you won't have naming conflicts with any names used in the
current file.
"""

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


#### Importing All Classes from a Module ####

from car import *


""""
This method is not recommended for two reasons. First, it's helpful to be
able to read the import statements at the top of a file and get a clear sense of
which classes a program uses. With this approach it's unclear which classes
you’re using from the module. This approach can also lead to confusion
with names in the file. If you accidentally import a class with the same name
as something else in your program file, you can create errors that are hard
to diagnose.

If you need to import many classes from a module, you're better off
importing the entire module and using the module_name.ClassName syntax.
You won't see all the classes used at the top of the file, but you'll see clearly
where the module is used in the program. You'll also avoid the potential
naming conflicts that can arise when you import every class in a module.

"""
