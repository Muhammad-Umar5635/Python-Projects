def main():
    while True:
        try:
            # Make sure to cast the input to a float so we can do math with it!
            num: float = float(input("Enter a number to see its square: ")) 
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    # Print out the square
    print(str(num) + " squared is " + str(num ** 2)) 


# There is no need to edit code beyond this point

if __name__ == "__main__":
    main()