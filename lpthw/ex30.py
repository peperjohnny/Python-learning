## set variables
people = 50
cars = 40
trucks = 150

## checks if there are more cars than people
if cars > people:
    ## prints out the following if there are more cars than People
    print "We should take the cars."
## if the first check is not true it defaults to the next
## checks if there are more people than cars
elif cars < people:
    ## prints out the following if there are less cars than People
    print "We should not take the cars."
## if both logic tests are incorrect the following is run
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
