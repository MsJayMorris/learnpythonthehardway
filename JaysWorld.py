print 'Welcome to Sirrom!'

print "You pull into the driveway. You have two options."
print "1. Go into the house with Lox the monkey on the front porch."
print "2. Go into the garage with Smokey the giant bear."

option = raw_input("> ")

if option == "1":
	print "Lox is in the mood for a drink."
	print "Jack and Coke coming up!!!!"
	
elif option == "2":
	print "Smokey needs to shampoo his fur...."
	print "I know you hit Sampson this week."
	print "1. Either give up the shampoo."
	print "2. Smokey is going to eat you!"
	
	give = raw_input("> ")
		
	if give == "1":
		print "That's right sucka. You know what it is."
	elif give == "2":
		print "Num num num.... You are delicious."
		print "Sorry homie, you should have passed the shampoo!"
		
else:
	print "Chicken shit!"
