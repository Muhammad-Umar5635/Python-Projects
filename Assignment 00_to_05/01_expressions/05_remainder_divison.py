def main():
    while True:
        try:
            number1 = int(input("Please Enter an integer to be divided: "))
            number2 = int(input("Please Enter an integer to divide by: "))
            if number1 > 0 and number2 > 0:
                remainder = number1 % number2
                quotient = number1 // number2
                print(f"The remainder when {number1} is divided by {number2} is: {remainder}")
                print(f"The quotient when {number1} is divided by {number2} is: {quotient}")
                print(f"The result of this Division is {quotient} with a remainder of {remainder}")
                break
            else:
                print("Invalid input. Please enter positive numbers.")
                continue
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            continue

if __name__ == "__main__":    
    main()