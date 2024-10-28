import random

def roll_dice():
    qnt = int(input("Enter the quantity of dices: "))
    for i in range(qnt):
        print(f"Dado {i + 1}: {random.randint(1,6)}")

if __name__ == "__main__":
    roll_dice()