
############# Classes #############

# Basics

"""
Classes have methods and attributes. Variables in the class which are accessible 
through instances are called attributes (defined with self. as the prefix which also
makes those variables accessible through all methods of the class). Functions in the 
class are called methods and properties as functions applies to methods as well with 
the only practical difference of how we call the methods. 

The __init__() method is a special method that Python runs automatically whenever we 
create a new instance based on the class. This method has two leading underscores and 
two trailing underscores, a convention that helps prevent Python's default method names 
from conflicting with your method names. Make sure to use two underscores on each side 
of __init__(). If you use just one on each side, the method won't be called automatically 
when you use your class, which can result in errors that are difficult to identify.

We define the __init__() method to have three parameters: self, name, and age. The self 
parameter is required in the method definition, and it must come first before the other 
parameters. It must be included in the definition because when Python calls this method 
later (to create an instance), the method call will automatically pass the self argument. 
Every method call associated with an instance automatically passes self, which is a reference 
to the instance itself; it gives the individual instance access to the attributes and methods 
in the class. E.g. When we make an instance of Dog, Python will call the __init__() method from 
the  Dog class. We'll pass Dog() a name and an age as arguments; self is passed automatically, 
so we  don't need to pass it. Whenever we want to make an instance from the Dog class, wel'l 
provide  values for only the last two parameters, name and age.
"""

# Styling Guidelines

"""
Class names should be written in CamelCase. To do this, capitalize the
first letter of each word in the name, and don't use underscores. Instance
and module names should be written in lowercase with underscores between
words.
Every class should have a docstring immediately following the class definition.
The docstring should be a brief description of what the class does,
and you should follow the same formatting conventions you used for writing
docstrings in functions. Each module should also have a docstring describing
what the classes in a module can be used for.
You can use blank lines to organize code, but don't use them excessively.
Within a class you can use one blank line between methods, and
within a module you can use two blank lines to separate classes.
If you need to import a module from the standard library and a module
that you wrote, place the import statement for the standard library module
first. Then add a blank line and the import statement for the module you
wrote. In programs with multiple import statements, this convention makes
it easier to see where the different modules used in the program come from.
"""

class Car:
    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ 
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading. """
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """ Fill the gas tank. """
        print("Gas tank is now full!")


class Battery:
    """ A simple attempt to model a battery for an electric car. """

    def __init__(self, battery_size=75):
        """ Initialize the battery's attributes. """
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """ 
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)  # This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. It is a special function that allows you to call a method from the parent class. The name super comes from a convention of calling the parent class a superclass and the child class a subclass.
        # self.battery_size = 75
        self.battery = Battery()  # Instances as Attributes

    # def describe_battery(self):
    #     """ Print a statement describing the battery size. """
    #     print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """ 
        Electric cars don't have gas tanks.
        Created this method to override this method from the Parent Class.
        """
        print("This car doesn't need a gas tank!")


############# Experiments Start #############

exp = 3

if exp == 1:
    #### To create an instance of the class ####
    my_new_car = Car('audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())

    #### To update odometer ####
    ## Modifying an Attribute’s Value Directly
    # my_new_car.odometer_reading = 23

    ## Modifying an Attribute’s Value Through a Method
    my_new_car.update_odometer(23)
    # my_new_car.update_odometer(12)

    my_new_car.read_odometer()
elif exp == 2:
    my_used_car = Car('subaru', 'outback', 2015)
    print(my_used_car.get_descriptive_name())

    my_used_car.update_odometer(23_500)
    my_used_car.read_odometer()
    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()
elif exp == 3:
    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.fill_gas_tank()
    # my_tesla.describe_battery()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()

############# Experiments End #############
