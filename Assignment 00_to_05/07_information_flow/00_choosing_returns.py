def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            if is_adult(age):
                print("You are an adult.")
            else:
                print("You are not an adult.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()