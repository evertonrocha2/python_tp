def guess_game():
    secret_number = 7
    guess = int(input("Guess a number: "))
    
    if guess == secret_number:
        print("You win!")
    elif guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

if __name__ == "__main__":
    guess_game()