def double(num: int):
  return num * 2

# There is no need to edit code beyond this point

def main():
  while True:
    print("This program doubles the number you enter.")
    try:
      num = int(input("Enter a number: "))
      num_times_2 = double(num)
    except ValueError:
      print("Please enter valid number.")
      continue
    print("Double that is", num_times_2)
    break

if __name__ == '__main__':
    main()