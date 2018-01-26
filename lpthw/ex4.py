# defines the variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

# defines a variable by subtraticting two variables from each other
cars_not_driven = cars - drivers

# defines a variable as a diffrent variable
cars_driven = drivers

# defines a variable by multiplying two variables
carpool_capacity = cars_driven * space_in_a_car

# defines a variable by dividing two variables
average_passengers_per_car = passengers / cars_driven


# prints a bit of text, calls for a variable and prints a bit of text
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
