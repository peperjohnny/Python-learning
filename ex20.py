## argv import as always
from sys import argv

script, input_file = argv
## create a function  to print a read file
def print_all(f):
    print f.read()
## set opened file to 0 as reading back from first character
def rewind(f):
    f.seek(0)
## print a line of the file with line number and actual file line
def print_a_line(line_count, f):
    print line_count, f.readline()
## open up a file
current_file = open(input_file)
## print the whole file
print "First let's print the whole file:\n"

print_all(current_file)
## set the file cound back to character 1
print "Now let's rewind, kind of like a tape."

rewind(current_file)
## set 1 and print the first line of text
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
#print "%d" % current_line
## increment line number and print next line of file
current_line += 1
print_a_line(current_line, current_file)
#print "%d" % current_line
## increment line number once again and print next line of file
current_line += 1
print_a_line(current_line, current_file)
#print "%d" % current_line
