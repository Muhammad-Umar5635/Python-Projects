import math


def pythagorean_theorem(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
def main():
    while True:
        try:
            a = float(input("Enter the length of side \"AB\": "))
            b = float(input("Enter the length of side \"BC\": "))
            if a > 0 and b > 0:
                c = pythagorean_theorem(a, b)
                print(f"The length of the hypotenuse \"AC\" is: {c:.2f}")
                break
            else:
                print("Invalid input. Please enter positive values for both sides.")
                continue
        except ValueError:
            print("Invalid input. Please enter valid numbers for both sides.")
            continue

if __name__ == "__main__":
    main()