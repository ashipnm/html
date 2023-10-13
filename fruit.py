import random
fruit=input("enter the fruit:")
print("you select",fruit)
items=["apple","orange","mango","grape"]
f=random.choice(items)
print("guess the word:")
guesses = ''
turns = 6
while turns > 0:
	failed = 0
	for char in f:
		if char in guesses:
			print(char, end=" ")

		else:
			print("_")
			failed += 1

	if failed == 0:
		print("You Win")
		print("The word is: ", f)
		break
	print()
	guess = input("guess a character:")
	guesses += guess
	if guess not in f:
		turns -= 1
		print("Wrong")
		print("You have", + turns, 'more guesses')
		if turns == 0:
			print("You Loose")
