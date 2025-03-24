def main():
    while True:
        try:
            numbers = int(input("Enter number do you want to print even numbers: "))
            if numbers <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    Even_numbers = []
    i = 0
    print("Even numbers are: ", end="")
    while True:
        if i % 2 == 0:
            Even_numbers.append(i)
            if len(Even_numbers) == numbers:
                break
        i += 1
        
    print(Even_numbers)


if __name__ == "__main__":
    main()
