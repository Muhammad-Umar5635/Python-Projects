def main():
    def get_last_element(lst):
        return lst[len(lst)-1]
    def get_lst():
        lst = []
        while True:
            element = input("Enter an elemet of the list or type 'stop' to stop : ")
            if element.lower() == "stop":
                if lst == []:
                    print("list is empty. Enter an element of the list: ")
                    continue
                else:
                    break
            elif element == "":
                print("Enter an element of the list.")
                continue
            elif element.lower() != "stop":
                lst.append(element)
                continue

        return lst
        
    lst = get_lst()
    print("The last element of the list is:",list(get_last_element(lst)))

if __name__ == "__main__":
    main()