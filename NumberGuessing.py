import random


print("""Welcome to the Number Guessing Game!
Try to guess the number between 1 and 100.
You can leave from the game by typing 'exit' command.""")

#Random Number Generation
print()#Adding a blank line
target_num=random.randint(1,100)


count=1
while True:
#User Input for the number guessing game
    guess_num=input("Enter your guess: ")
    #guess_num=int(guess_num)
    if guess_num.isdigit():
        guess_num = int(guess_num)
        if target_num==guess_num:
            print(f"Congratulations! You've guessed the number in {count} attempts")
            #If the user want to play again
            replay = input("Do you want to play again? (yes/no): ").lower()
            if replay == "yes":
                target_num = random.randint(1, 100)
                count = 1
                continue
            else:
                break
           # break

        elif target_num > guess_num:
            print("Too low!")
        elif target_num < guess_num:
            print("Too high!")

        count += 1
        print() # This will print blank line after each guess
    else:
        if guess_num.lower()=="exit":
            print(f"Game Over! See you on the next time. The number was {target_num}.")
            print()
            #If the user want to play again
            replay=input("Do you want to play again? (yes/no): ").lower()
            if replay=="yes":
                target_num = random.randint(1, 100)
                count=1
                continue
            else:
                break
        else:
            print("Invalid Number! Please enter a valid number.")
            print()