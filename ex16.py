## modul argv import
from sys import argv
## write the name the file should have
script, filename = argv
## naming the file that is going to be worked on and was given upfront
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
## asking for enter or cancelling
raw_input("?")
## opening the file in write mode
print "Opening the file..."
target = open(filename, 'w')
## deleting file contents
print "Truncating the file. Goodbye!"
target.truncate()
## inputting 3 lines for the textdocument
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
## writing to the variable target, which is the opened txt file with a linebreak
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
## closing the file as it is not being worked on anymore
print "And finally, we close it."
target.close()
