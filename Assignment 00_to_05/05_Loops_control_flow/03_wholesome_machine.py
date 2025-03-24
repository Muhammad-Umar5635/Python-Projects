def main():
    Affirmation = "I am capable of doing anything I put my mind to."
    print("The affirmation is: \n"+Affirmation)
    while True:
        user_input = input("Please type the following affirmation: ")
        if user_input == Affirmation:
            print("Thanks for the affirmation.")
            break
        else:
            print("That was not the affirmation. ")
            continue


if __name__ == "__main__":
    main()