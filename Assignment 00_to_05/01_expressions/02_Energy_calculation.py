def main():
    c= 299792458 #speed of light in m/s
    while True:
        try:
            mass_in_kg = float(input("Enter mass in kilograms: "))
            if mass_in_kg <=0:
                print("Invalid input.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input.")
            continue
    energy_in_joules = mass_in_kg * (c**2)
    print("e = m * c^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"c = {c} m/s")
    print(f"Energy in joules: {energy_in_joules}")

if __name__ == "__main__":
    main()
