def main():
  while True:
    try:
      User_input = int(input("Enter a number: "))
      if User_input > 0:
        break
      else:
        print("Please enter positive number.")
        continue
    except ValueError:
      print("Please enter valid number.")
      continue
  lst = []
  for i in range(1, User_input + 1):
    if User_input % i == 0:
      lst.append(i)
  print("The factors of", User_input, "are", lst)

if __name__ == "__main__" :
	main()
