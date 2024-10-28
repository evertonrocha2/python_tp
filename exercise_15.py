def interative_story():
    choice = input("Do you want to go to the left or right? ")
    if choice == "left":
        print("You fell into the trap")
    elif choice == "right":
        print("You got a treasure")

if __name__ == "__main__":
    interative_story()