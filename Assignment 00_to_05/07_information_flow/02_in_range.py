def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    else:
        return False
    
def main():
    while True:
        try:
            n = int(input("Enter a number: "))
            low = int(input("Enter a low number: "))
            high = int(input("Enter a high number: "))
            print(in_range(n, low, high))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
if __name__ == "__main__":
    main()