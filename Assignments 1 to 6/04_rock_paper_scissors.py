def play():
    import random
    Computer_guess=random.choice(["r","p","s"])
    while True:
        user_choice=input("Enter your choice \"r\" for rock, \"p\" for paper and \"s\" for scissor: ")
        if user_choice not in ["r","p","s"]:
            print("Enter a valid choice")
            continue
        if user_choice==Computer_guess:
            print("Tie! Both chose: ",user_choice)
            break
        elif (user_choice=="r" and Computer_guess=="s") or (user_choice=="s" and Computer_guess=="p") or (user_choice=="p" and Computer_guess=="r"):
            print("You win! Computer chose: ",Computer_guess)
            break
        else:
            print("You lose! Computer chose: ",Computer_guess)
            break

play()