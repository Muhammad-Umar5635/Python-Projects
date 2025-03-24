def main():
    def double_list(list):
        return [i** 2 for i in list]
    while True:
        try:
            lst = input("Enter a list of numbers (e.g., 1,2,3): ")
            lst = [int(i.strip()) for i in lst.split(',')]
            break
        except ValueError:
            print("Invalid input. Please enter a list of numbers.")

    print(double_list(lst))

if __name__ == "__main__":
    main()