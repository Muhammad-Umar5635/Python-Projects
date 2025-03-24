Inches_In_Foot = 12

def main():
    while True:
        try:
            feet = float(input("Enter the number of feet: "))
            if feet > 0:
                inches = feet * Inches_In_Foot
                print(f"{feet} feet is equal to {inches} inches.")
                break
            else:
                print("Invalid input. Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

if __name__ == "__main__":
    main()