#string Concatination
def madlibs():
    Adjective = input("Enter an Adjective: ")
    Verb = input("Enter a Verb: ")
    Noun = input("Enter a Noun: ")
    Adjective2 = input("Enter another Adjective: ")
    Noun2 = input("Enter another Noun: ")
    Story = f"One sunny day, a {Adjective} squirrel decided to {Verb} up the tallest {Noun} \
in the forest. As it climbed, it noticed a {Adjective2} cloud shaped like a {Noun2} \
that was floating in the sky. The squirrel couldn’t believe its eyes and started \
to chattering excitedly. Suddenly, a gust of wind blew, and the squirrel had to hold \
on tightly to avoid falling. After the adventure, it scurried back down, feeling proud \
of its {Adjective} accomplishment. The end!"

    print(Story)

madlibs()