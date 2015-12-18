cars = 100.0
space_in_a_car = 4.0
drivers = 30.0
passengers = 90.0
cars_not_driven = cars - drivers
cars_driven = drivers
#In the first version car_pool_capacity was carpool_capacity so the program failed at line 15
car_pool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are ", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", car_pool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


