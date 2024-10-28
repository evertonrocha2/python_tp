def calculate_imc():
    weight = float(input("Enter you weight in kg:"))
    height = float(input("Enter you height in m:"))
    imc = weight / (height * height)
    print("Your IMC is:", imc)

    if imc < 18.5:
        print("You're underweight")
    elif imc < 24.9:
        print("You're normal weight")
    elif imc < 29.9:
        print("You're overweight")
    else: 
        print("You're obese")

if __name__ == "__main__":
    calculate_imc()