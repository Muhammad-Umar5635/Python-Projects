def main():
    def sum_of_list(list):
        sum = 0
        for i in list:
            sum += i
        return sum
    while True:
        try:
            lst = input("Enter a list of numbers (e.g., 1,2,3): ")
            lst = [int(i.strip()) for i in lst.split(',')]
            break
        except ValueError:
            print("Invalid input. Please enter a list of numbers.")

    print(sum_of_list(lst))

if __name__ == "__main__":
    main()