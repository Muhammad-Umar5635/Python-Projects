import random

def password_generator():
    while True:
        try:
            passwords = int(input("Enter the number of passwords you want to generate: "))
            if passwords <= 0:
                print("Please enter a positive number!")
                continue
            
            length = int(input("Enter the length of each password: "))
            if length <= 0:
                print("Password length must be greater than 0!")
                continue

            break  # Exit loop if input is valid

        except ValueError:  
            print("⚠️ Enter a valid number!")

    # Characters allowed in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-=,./?;:[]{}()!@#$%^&*"

    print("\nGenerated Passwords:")
    for i in range(passwords): 
        password = "".join(random.choices(characters, k=length))  
        print(f"{i+1}. {password}")

# Run the function
password_generator()
