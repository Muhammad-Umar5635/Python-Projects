import random

def main():
    while True:
        try:
            numbers = int(input("Enter number do you want to print random numbers: "))
            if numbers <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    lst = set()
    while len(lst) < numbers:
        lst.add(random.randint(1, 100))
    print(lst)

if __name__ == "__main__":
    main()
