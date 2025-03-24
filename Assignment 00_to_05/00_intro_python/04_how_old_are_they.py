#This is a age-related riddle program!
# Anton's age is given as __ years old
# Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
# Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
# Drew is as old as Chen's age plus Anton's age, so add them together
# Ethan is the same age as Chen, so set Ethan's age equal to Chen's
def main():
    while True:
        try:
            anton = int(input("Enter Anton's age: "))
            if anton <=0:
                print("Age never be Negative or Zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    beth : int = 6 + anton  
    chen : int = 20 + beth  
    drew  : int= chen + anton  
    ethan : int = chen  

   # Print out all of the ages!
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))


if __name__ == "__main__":
    main()