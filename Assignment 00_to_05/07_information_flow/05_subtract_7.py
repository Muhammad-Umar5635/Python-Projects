def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            print("The output after subtracting 7:",num - 7)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()