import random
items=["rock","paper","scissor"]
choice=input("Choose rock,paper or scissor:")
cs=random.choice(items)
print("You choose",choice)
print("Computer choose",cs)
if choice=="rock" and cs=="scissor":
    print("You win")
elif choice=="scissor" and cs=="paper":
    print("You win")
elif choice=="paper" and cs=="rock":
    print("You win")
elif choice==cs:
    print("Tie")
else:
    print("Computer win")                                                 