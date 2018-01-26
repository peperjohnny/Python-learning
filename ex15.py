## the ARGV Module is being loaded
from sys import argv
## argv shall spit out the name of the script and the variable filename,
## which you input while starting the programm
script, filename = argv
## set variable txt as a opened file
txt = open(filename)
## outputting the file contents
print "Here's your file %r:" % filename
## outputs the actual file content
print txt.read()
## retype in the filename to output it once again
print "Type the filename again:"
## set variable as file_again from taking an input
file_again = raw_input("> ")
## opening inputed file and setting it as a variable
txt_again = open(file_again)
## outputting the content again
print txt_again.read()
txt.close()
txt_again.close()
