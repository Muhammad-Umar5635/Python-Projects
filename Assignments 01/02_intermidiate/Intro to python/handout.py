def main():
    while True:
        try:
            weight_on_earth = float(input("Enter a weight on earth: "))
            break
        except ValueError:
            print("Enter a valid number.")
            continue
    weight_on_mars = weight_on_earth * 0.378
    weight_on_jupiter = weight_on_earth * 2.36
    weight_on_venus = weight_on_earth * 0.889
    weight_on_mercury = weight_on_earth * 0.376
    weight_on_saturn = weight_on_earth * 1.081
    weight_on_uranus = weight_on_earth * 0.815
    weight_on_neptune = weight_on_earth * 1.14
    planets = ["Mars", "Jupiter", "Venus", "Mercury", "Saturn", "Uranus", "Neptune"]
    print(planets)
    while True:
        try:
            planet = input("Enter a planet: ").capitalize()
            if planet not in planets:
                raise ValueError
            break
        except ValueError:
                print("Enter a valid planet.")
                continue
    if planet == "Mars":
        print(f"Your weight on {planet} is:  {weight_on_mars:.2f}")
    elif planet == "Jupiter":
        print(f"Your weight on {planet} is: {weight_on_jupiter:.2f}")
    elif planet == "Venus":
        print(f"Your weight on {planet} is: {weight_on_venus:.2f}")
    elif planet == "Mercury":
        print(f"Your weight on {planet} is: {weight_on_mercury:.2f}")
    elif planet == "Saturn":
        print(f"Your weight on {planet} is: {weight_on_saturn:.2f}")
    elif planet == "Uranus":
        print(f"Your weight on {planet} is: {weight_on_uranus:.2f}")
    elif planet == "Neptune":
        print(f"Your weight on {planet} is: {weight_on_neptune}:.2f")

if __name__ == "__main__":
    main()
    