numbers = []

print "How long do you want this list? Less than 20 please."
length = int(raw_input("> "))

print "What interval do you want the list to increase?"
interval = int(raw_input("> "))
	
def list(length, interval):
	i = 0
	
	while i < length:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + interval
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
list(length, interval)

print "The numbers: "

for num in numbers:
	print num