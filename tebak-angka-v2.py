import random

def quiz(max=5):
	calc = 0
	print(random_number)
	while True:
		number = int(input("Guess Number You Think: "))
		if number == random_number:
			print("Your Guess is True")
			print("Your Wrong is: ", (calc))
			break
		elif random_number > number:
			calc += 1
			print("Your Guess is too Low")
		elif random_number < number:
			calc += 1
			print("Your Guess is too High")
		else:
			print("Bad")
		if calc == max:
			print(f"Limit Your Guess, the number true is: ", (random_number))
			break

print("Welcome to Guess The Number")
while True:
	level = str(input("Select Level (easy, medium, hard): "))
	if level == "easy":
		random_number = random.randint(1,51)
		print("The number between 1-50")
		quiz()
	elif level == "medium":
		random_number = random.randint(1,101)
		print("The number between 1-101")
		quiz()
	elif level == "hard":
		random_number = random.randint(1,501)
		print("The number between 1-501")
		quiz()
	else:
		print("Your Input Incorrect")