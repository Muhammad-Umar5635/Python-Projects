while True:
    try:
        VALUE = int(input("Enter the number of terms you want in the Fibonacci Series: "))
        if VALUE <= 0:
            print("Enter a positive number")
            continue
        break
    except ValueError:
        print("Enter a valid number")
        continue

def main():
    lst = []
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while len(lst) <= (VALUE-1):
        lst.append(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
    print("The Fibonacci Series is: ", lst)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()