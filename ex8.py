formatter = "%r %r %r %r"


# print variable and input the raw with the following
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# " ' will be used to show this printout ' for 1,2,4 and " for 3 because a ' is used in the sentence
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
