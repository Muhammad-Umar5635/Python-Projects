def main():
    while True:
        try:
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    celsius = (fahrenheit - 32) * 5/9

    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()