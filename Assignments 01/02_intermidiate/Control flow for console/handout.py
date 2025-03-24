import random

def main():
    score = 0
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    for i in range(1,6):
        print(f"Round {i}:")
        while True:
            try:
                user_input = int(input("Your number is: "))
                break
            except ValueError:
                print("Enter a valid number")
                continue
        computer_number = random.randint(1, 100)
        while True:
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
            if guess in ["higher", "lower"]:
                break
            else:
                print("Please write either 'higher' or 'lower'.")
        if guess == "higher":
            if user_input < computer_number:
                print("You were right! The computer's number was", computer_number)
                score += 1
                print("Your score is now", score)
            else:
                print("Aww, that's incorrect. The computer's number was", computer_number)
                print("Your score is now", score)  
        elif guess == "lower":
            if user_input > computer_number:
                print("You were right! The computer's number was", computer_number)
                score += 1
                print("Your score is now", score)
            else:
                print("Aww, that's incorrect. The computer's number was", computer_number)
                print("Your score is now", score)
        else:
            print("Invalid input. Please try again.")
    
    print("Game over! Your final score is", score)
    if score == 5:
        print("Wow! You played perfectly!")
    elif score>=2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")
    print("Thanks for playing!")
if __name__ == "__main__":
    main()
