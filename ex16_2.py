from sys import argv

script, filename = argv

print "This script is intented to show you the contents of the file created in ex 16."

txt = open(filename)

print "Here are your filecontents."

print txt.read()
txt.close()
