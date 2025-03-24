def main():
  while True:
    try:
        User_input = int(input("Enter a number: "))
        print("The ones digit is :",User_input % 10)
        break
    except ValueError:
      print("Please enter valid number.")
      continue
if __name__ == "__main__" :
	main()