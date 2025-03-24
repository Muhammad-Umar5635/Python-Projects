#Problem Statement
#Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            if num >= 100 or num < 0:
                print("The number is must be in between 0 and 100.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")
            continue  
    
    while num < 100:
        print(f'The double of {num} is {num * 2}')
        num *= 2
if __name__ == "__main__":
    main()  
    