def main():
  lst = []
  even_number = 0
  odd_number = 0
  while True:
      number = input("Enter an integer or press enter to stop: ")
      if number == "":
        break
      if number.isalpha() or int(number) < 0:
        print("Please enter valid or positve number.")
        continue
      else:
        number = int(number)
        lst.append(number)
        if number % 2 == 0:
          print(number, "This is Even number")
          even_number +=1
        else:
          print(number, "This is Odd number")
          odd_number +=1
  print("Your given number list: ", lst)
  print("Number of even number in the list", even_number)
  print("Number of odd number in the list", odd_number)
if __name__ == "__main__" :
	main()