## creates a function with which something will be put out as soon as the function is called
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

## values are simply set in the parenthesis
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

## set variables first and then print them
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

## do some math and call the function on this one
print "We can even do math inside too:"
cheese_and_crackers(10+ 20, 5 + 6)

## use variables and use math on them before calling the function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
