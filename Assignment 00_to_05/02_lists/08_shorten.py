def main():

    Length_of_list = int(input("Please enter the maximum length of the list: "))

    def shorten(lst):
        while len(lst) > Length_of_list:
            last_elem = lst.pop()
            print("Deleted element:", last_elem)
        print(lst)

# There is no need to edit code beyond this point

    def get_lst():
        """
        Prompts the user to enter one element of the list at a time and returns the resulting list.
        """
        lst = []
        elem = input("Please enter an element of the list or press enter to stop. ")
        while elem != "":
            lst.append(elem)
            elem = input("Please enter an element of the list or press enter to stop. ")
        return lst

    lst = get_lst()
    shorten(lst)

if __name__ == "__main__":
    main()