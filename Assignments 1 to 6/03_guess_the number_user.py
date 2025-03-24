import random

def play():
    count = 0
    while True:
        try:
            user_number = int(input("Enter a number b/w 1 and 100: "))
            if user_number < 1 or user_number > 100:
                print("Enter a number between 1 and 100")
                continue
            break
        except ValueError:
            print("Enter a valid number")
            continue
    low = 1
    high = 100
    while True:
        computer_guess = random.randint(low, high)
        if computer_guess == user_number:
            print("Computer guessed! The number was: ", computer_guess)
            print("Computer guessed it in: ", count+1, "tries")
            break
        elif computer_guess < user_number:
            print(f"Computer guess is Too low! {computer_guess}")
            count += 1
            low = computer_guess + 1
        elif computer_guess > user_number:
            print(f"Computer guess is Too high!: {computer_guess}")
            count += 1
            high = computer_guess - 1

if __name__ == "__main__":
    play()