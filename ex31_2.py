print "You are in front of a castle.\nDo you want to go in yes or no?"

castle = raw_input("> ")

if castle == "yes":
    print "You try the door handle but it won't budge."
    print "Do you want to kick the door in yes or no?"

    door = raw_input("> ")

    if door == "yes":
        print "You give it all, but alas it still won't budge."
        print "Do you want to run against it with your whole body yes or no?"

        body = raw_input("> ")

        if body == "yes":
            print "A moment before you hit door it opens and you stumble into a pit with hundreds of adventurers making the same Mistake you did."
        elif body == "no":
            print "You are still hurting from the kick and lie down to rest and contemplate life."
        else:
            print "You turn around and walk away, living a fullfilling life."
    else:
        print "You turn around and walk away. Something seems strange about the castle and you don't want to find out."
elif castle =="no":
    print "Some things are better left undiscovered."

else:
    print "Sometimes not playing is the key to winning."
