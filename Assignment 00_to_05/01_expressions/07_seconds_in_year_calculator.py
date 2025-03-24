def main():
    while True:
        try:
            year = int(input("Enter a year: "))
            if year >=1:
                seconds_in_year =year * 365 * 24 * 60 * 60
                print(f"There are {seconds_in_year} seconds in {year} year.")
                break
            else:
                print("Invalid input. Please enter a year greater than or equal to 1.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid year.")
            continue

if __name__ == "__main__":
    main()  