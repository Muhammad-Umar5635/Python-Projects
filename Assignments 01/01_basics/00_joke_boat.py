def main():
    while True:
        User_input = input("What do you want? ").strip().lower()
        if "joke" in User_input :
            print( 'Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: \'because they had eggs\'')
            break
        else:
            print("No joke for you, Sorry I only tell jokes.")
            continue

if __name__ == "__main__": 
    main()