def main():
  string = str(input("Please type a message: "))
  while True:
    try:
      number = int(input("Enter a number of times to repeat your message: "))
      if number <= 0:
         print("Please enter positive number.")
      break
    except ValueError:
      print("Please enter valid number.")
  print(string * number)

if __name__ == "__main__" :
	main()