

num = int(raw_input("Type in a number to loop: "))

def loopy(num):
    i = 0
    numbers = []
    x = int(raw_input("Increment by: "))
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + x
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


        print "The numbers: "

    for i in range(0, x):
        print "Adding %d to the list." % i

loopy(num)
