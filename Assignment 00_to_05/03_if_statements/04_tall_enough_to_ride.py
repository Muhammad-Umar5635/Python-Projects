def main():
  while True:
    try:
      height  = str(input("How tall are you? "))
      if height == "":
        print()
        break
      if height.isalpha():
        print("Invalid output")
        continue
      elif float(height) < 0:
        print("Height never be in negetive.")
        continue
      elif float(height) < 50:
        print("You're not tall enough to ride, but maybe next year!")
        continue
      elif float(height) >= 50:
        print("You're tall enough to ride!")
        continue
    except ValueError:
      print("Invalid output")
      continue
if __name__ == "__main__":
	main()