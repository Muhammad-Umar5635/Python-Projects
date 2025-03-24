import random

def hangman_game():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango",
             "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "yuzu"]
    
    word = random.choice(words)  # Select a random word
    guessed_letters = []
    attempts = 6  # Number of attempts

    while attempts > 0:
        # Display the word with guessed letters
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print("\nGuess the word:", display_word)

        # Check if the user has won
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

        # Get user input
        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print("🔄 You already guessed that letter!")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess in word:
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! You have {attempts} attempts left.")

    # If the loop ends, the player has lost
    print("\n💀 Game Over! The word was:", word)

# Run the game
hangman_game()

