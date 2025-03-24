def main():
    PETURKSBOUIPO_AGE : int = 16
    STANLAU_AGE : int = 25
    MAYENGUA_AGE : int = 48

    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
            continue

      # Check if the user can vote
    if age >= MAYENGUA_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}. You can vote in stanlau where the voting age is {STANLAU_AGE}.You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

    elif age >= STANLAU_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}. You can vote in stanlau where the voting age is {STANLAU_AGE}. You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

    elif age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}. You cannot vote in stanlau where the voting age is {STANLAU_AGE}. You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.") 

    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16. You cannot vote in stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")

if __name__ == "__main__":
    main()