#define number of people and things
people = 30
cars = 40
buses = 15

#compares if there are more cars vs people and decision process
if cars > people:
	print "We should take the cars."
#if less cars then people then print this
elif cars < people:
	print "We should not take the cars."
#if conditions above are not met, then print this
else:
	print "We can't decide."

#compares more buses to less cars and prints result
if buses > cars:
	print "That's too many buses."
#compares less buses to more cars and prints result
elif buses < cars:
	print "Maybe we could take the buses."
#if conditions above are not met, then print this
else:
	print "We still can't decide."

#compares more people to less buses, prints result
if people > buses:
	print "Alright, let's just take the buses."
#if conditions above are not met, then print this
else:
	print "Fine, let's stay home then."