secretNumber=5
guess=0
while guess!=secretNumber:
    guess=int(input("Enter your guess"))
    if guess>secretNumber:
        print("OHHH your number is greater")
    elif guess<secretNumber:
        print("OHHH your number is smaller")
print("Correct answer")
     