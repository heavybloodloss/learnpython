# setting the format for the entire list of things
formatter = "%r %r %r %r"

# printing some numbers in the correct format
print formatter % (1, 2, 3, 4)
# printing some numbers in the form of words
print formatter % ("one", "two", "three", "four")

# printing some True/False statements
print formatter % (True, False, False, True)

# printing format 4 times
print formatter % (formatter, formatter, formatter, formatter)

# printing these statements in the proper format
# this won't work without the proper number of arguments, i.e. 4
# tested with 3 arguments; 
# yup, TypeError: not enough arguments for format string
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)