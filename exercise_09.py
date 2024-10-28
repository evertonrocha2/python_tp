def apply_discount(value):
    if value > 500:
        discount = 0.25
    elif value > 200:
        discount = 0.15
    elif value > 100:
        discount = 0.10
    else:
        discount = 0 
    return value * ( 1 - discount)

if __name__ == "__main__":
    buy_value = float(input("Enter the value of the buy: "))
    print("The value after discount is:", apply_discount(buy_value))

