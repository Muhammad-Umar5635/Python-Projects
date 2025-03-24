def main():
    # Prompt the user to enter two numbers
    while True:
        # Try to convert the input to an integer
        try:
            num_1 = int(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    while True:
        # Try avoiding exceptions
        try:
            num_2 = int(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    sum = num_1 + num_2

    print(f"Sum of {num_1} and {num_2} is {sum}")

if __name__ == "__main__":
    main()