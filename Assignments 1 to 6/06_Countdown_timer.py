import time

def countdown():
    while True:
        try:
            user_input = int(input("Enter the countdown time in seconds: "))
            if user_input <= 0:
                print("⚠️ Please enter a positive number!")
                continue
            break
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

    for i in range(user_input, 0, -1):
        print(f"\r⏳ Time remaining: {i} seconds ", end="", flush=True)
        time.sleep(1)

    print("\n⏰ Time's Up!")

# Run the countdown
countdown()
