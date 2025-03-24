def main():
    def get_last_element(lst):
        return lst
    def get_lst():
        lst = []
        while True:
            element = input("Enter a value : ")
            if element == "":
                break
            else:
                lst.append(element)
                continue
        return lst
        
    lst = get_lst()
    print("Here's the list:",list(get_last_element(lst)))

if __name__ == "__main__":
    main()