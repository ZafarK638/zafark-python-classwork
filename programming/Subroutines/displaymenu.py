def displayMenu():
  """Presents a menu to the user and validates their choice."""
  while True:
    print("\nMenu:")
    print("1. Add name")
    print("2. Display list")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    try:
      choice = int(choice)
      if 1 <= choice <= 3:
        return choice
      else:
        print("Invalid choice. Please enter a number between 1 and 3.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def addName(names):
  """Adds a name to the list at a specified location."""
  while True:
    try:
      location = int(input("Enter the list number to insert the name (1-10): "))
      if 1 <= location <= 10:
        name = input("Enter the name: ")
        names[location - 1] = name
        print("Name added successfully.")
        break
      else:
        print("Invalid location. Please enter a number between 1 and 10.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def displayList(names):
  """Displays the list of names."""
  print("\nList of names:")
  for i, name in enumerate(names):
    print(f"{i+1}. {name}")

# Initialize the list of names
names = ["" for _ in range(10)]

# Main program loop
while True:
  choice = displayMenu()

  if choice == 1:
    addName(names)
  elif choice == 2:
    displayList(names)
  elif choice == 3:
    print("Program terminating.")
    break
