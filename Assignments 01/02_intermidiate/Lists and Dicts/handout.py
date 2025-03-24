def main():
    list1 = ["apple", "banana", "orange", "grape" ,"pineapple"]
    print(list1)
    print("Add mango to the list")
    list1.append("mango")
    print(list1)
    print("lenght of list", len(list1))
    print("----Accessing elements----")
    while True:
        try:
            user_input = int(input("Enter index to access: "))
        except ValueError:
            print("Enter a valid number")
            continue
        if user_input <= len(list1)  and user_input > 0:
            print(list1[(user_input)-1])
            break
        else:
            print("Index out of range")
            continue
    print("----Modifying elements----")
    print(list1)
    while True:
        try:
            user_input = int(input("Enter index to Modify: "))
        except ValueError:
            print("Enter a valid number")
            continue
        if user_input <= len(list1) and user_input > 0:
            break
        else:
            print("Index out of range")
            continue
    list1[(user_input)-1] = input("Enter new value: ")
    print(list1)
    print("----Slicing the list----")
    print(list1)
    while True:
        try:
            user_input = int(input("Enter index to start slicing: "))
        except ValueError:
            print("Enter a valid number")
            continue
        if user_input <= len(list1)  and user_input > 0:
            break
        else:
            print("Index out of range")
            continue
    while True:
        try:
            user_input2 = int(input("Enter index to end slicing: "))
        except ValueError:
            print("Enter a valid number")
            continue
        if user_input2 <= len(list1) and user_input2 > 0 and user_input2 > user_input:
            break
        else:
            print("Index out of range or correct index to end slicing")
            continue
    print(list1[user_input-1:user_input2])    
if __name__ == "__main__":
    main()