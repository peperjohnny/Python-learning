# a variable is set as a string with a formator
x = "There are %d types of people." % 10
# variable as string set
binary = "binary"
do_not = "don't"
# variable as string set with formator put in from other variables
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# r is printed with ' automatically while s needs it manually
print "I said: %r." % x
print "I also said: '%s'." % y

# r calls for the last set variable
# r is for debugging purposes it shows raw data
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# printing two strings alongside
print w + e
