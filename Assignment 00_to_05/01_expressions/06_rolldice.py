import random
Num_sides = 6
# This program is used to show how variable scope works.
def roll_dice(numnber_of_times):
    total = 0
    for i in range(1,numnber_of_times + 1):
        random_number = random.randint(1,Num_sides) 
        print(f"{i}. Die number is : {random_number}")
        total += random_number
    print(f"Your Total score is :{total}")
def main():
    while True:
        try:
            numbers_of_times = int(input("Enter number you want to die roll :"))
            if numbers_of_times > 0:
                roll_dice(numbers_of_times)
                break
        except ValueError:
            print("Invalid input.")
            continue

if __name__ == "__main__":
    main()