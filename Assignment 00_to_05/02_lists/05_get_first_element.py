def main():
    def get_first_element(lst):
        return lst[0]
    def get_lst():
        lst = []
        element = input("Enter an elemet of the list or type 'stop' to stop: ")
        while element.lower() != "stop":
            lst.append(element)
            element = input("Enter an elemet of the list or type 'stop' to stop: ")
        return lst
    lst = get_lst()
    print("The first element of the list is:",get_first_element(lst))

if __name__ == "__main__":
    main()