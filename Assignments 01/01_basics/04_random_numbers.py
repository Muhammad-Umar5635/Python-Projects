import random
def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter a valid number.")
            continue
    lst = []
    for i in range(num):
        lst.append(random.randint(1, 100))
    print(lst)
if __name__ == "__main__":
    main()