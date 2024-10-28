def verify_maiority():
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are a child")
    else: 
        print("You are an adult")

if __name__ == "__main__":
    verify_maiority()