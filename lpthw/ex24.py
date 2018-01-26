print "Let's practice everything."
## \' to show ' in output. \ is an escape character'
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "__________"
print poem
print "__________"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

## function is created to call with a variable that is used later with a start_point
## started get's the value assigned of the variable it's called with
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000

## new and reused variables for output
beans, jars, crates = secret_formula(start_point)

## call for output by asking for the variables
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

## call for output by directly running the function
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
