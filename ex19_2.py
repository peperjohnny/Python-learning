def vacation_and_overtime(vacation_count,overtime_count):
    print "You have %d days of vacation." % vacation_count
    print "You have %d hours of overtime." % overtime_count
    print "Man that's enough to retire!"
    print "Get a tombstone.\n"


print "I'm giving the values in paranthesis."
vacation_and_overtime(20, 80)

print "Or I'm setting variables first, so I can reuse them later on."
amount_of_vacation = 10
amount_of_overtime = 30

vacation_and_overtime(amount_of_vacation, amount_of_overtime)

print "I could however, count them in the function."
vacation_and_overtime(10 + 10, 50 + 16)

print "Lastly I'll do both."
vacation_and_overtime(amount_of_vacation + 5, amount_of_overtime + 300)
