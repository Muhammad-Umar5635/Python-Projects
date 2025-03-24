def main():
    memory = {}
    while True:
        user_input = input("Enter a number or enter nothing to stop: ")
        if user_input == "":
            break
        if user_input in memory:
            memory[user_input] += 1
        else:
            memory[user_input] = 1

    for key, value in memory.items():
        print(f"{key} occurs {value} times")

if __name__ == "__main__":
    main()

