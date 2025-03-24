def main():
  while True:
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter Second number: "))
      break
    except ValueError:
     print("Please enter valid number.")
     continue
  Average = (num1 + num2) / 2
  print("The Average of two number is: ", Average)
if __name__ == "__main__" :
	main()