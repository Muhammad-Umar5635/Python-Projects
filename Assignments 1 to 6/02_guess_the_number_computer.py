import random

def play():
    count = 0
    my_number = random.randint(1, 99)
    while True:
        try:
            guess = int(input("I am thinking a number between 0 and 99... Enter a guess: "))
            break
        except ValueError:
            print("Enter a valid number")
            continue
    while True:
        if guess < my_number:
            print("Your guess is Too low!")
            count += 1
            try:
                guess = int(input("Enter a new number: "))
            except ValueError:
                print("Enter a valid number")
                continue
        elif guess > my_number:
            print("Too high!")
            count += 1
            try:
                guess = int(input("Enter a new number: "))
            except ValueError:
                print("Enter a valid number")
                continue
        if guess == my_number:
            print("Congratulations! The number was: ", my_number)
            print("You guessed it in: ", count+1, "tries") 
            break 

if __name__ == "__main__":
    play()