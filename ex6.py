#This section defines string variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#This section prints the string varibles
print x
print y

#This section shows the difference of using %r which prints everything in the variable where %s only prints the string
print "I said: %r." % x
print "I also said: %s." % y

hilarious = False

#The %r in this section requires a variable to be passed in when the variable joke_evaluation is printed
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#In this statement the '+' concatonates two variables.
print w + e
