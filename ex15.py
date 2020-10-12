# imports argv from standard dictionaries
from sys import argv

# calls script name and assigns filename
script, filename = argv

# puts the .txt filename provided in a useful format
txt = open(filename)

# prints the name of the file user provided
print "Here's your file %r:" % filename

# prints the entirety of selected .txt file
print txt.read()

# closes file
txt.close()

# asks for filename to print again
print "Type the filename again:"

# takes raw_input from user for new .txt file
file_again = raw_input("> ")

# puts user_input into useable format
txt_again = open(file_again)

# prints results
print txt_again.read()

# closes file
txt_again.close()