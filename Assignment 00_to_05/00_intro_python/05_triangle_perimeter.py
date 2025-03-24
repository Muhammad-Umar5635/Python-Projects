def main():
    # Get the 3 side lengths of the triangle
    while True:
        try:
            side1: float = float(input("What is the length of side 1? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    while True:
        try:    
            side2: float = float(input("What is the length of side 2? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    while True:
        try:
            side3: float = float(input("What is the length of side 3? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    # Print out the perimeter
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))


# There is no need to edit code beyond this point

if __name__ == "__main__":
    main()