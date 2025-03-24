sentence_start = "Panaversity is fun. I learned to program and used Python to make my"
def main():
    Adjective = str(input("Please type an adjective and press enter: "))
    Noun = str(input("Please type a noun and press enter: "))
    Verb = str(input("Please type a verb and press enter: "))
    print(f"{sentence_start} {Adjective} {Noun} {Verb}!")

if __name__ == "__main__":
    main()
