# Initialize the car park grid
ROWS = 10
COLUMNS = 6

# Function to reset all spaces in the car park to "empty"
def empty_car_park(car_park):
    for row in range(ROWS):
        for col in range(COLUMNS):
            car_park[row][col] = "empty"

# Function to park a car
def park_a_car(car_park):
    reg_number = input("Enter the car registration number: ")
    
    # Get row and column input
    row = int(input("Enter the row number (1-10): ")) - 1  # Adjust for 0-based index
    col = int(input("Enter the column number (1-6): ")) - 1  # Adjust for 0-based index
    
    if car_park[row][col] == "empty":
        car_park[row][col] = reg_number
        print(f"Car parked successfully at grid reference [{row + 1}, {col + 1}]")
    else:
        print("Space is occupied. Please enter a different grid reference.")

# Function to remove a car
def remove_a_car(car_park):
    reg_number = input("Enter the car registration number to remove: ")
    found = False

    for row in range(ROWS):
        for col in range(COLUMNS):
            if car_park[row][col] == reg_number:
                car_park[row][col] = "empty"
                print(f"Car with registration {reg_number} has been removed from grid reference [{row + 1}, {col + 1}]")
                found = True
                break  # Exit inner loop
        if found:
            break  # Exit outer loop

    if not found:
        print(f"Car with registration {reg_number} not found.")

# Function to display the car park grid
def display_car_park_grid(car_park):
    print("Current Car Park Grid:")
    for row in range(ROWS):
        for col in range(COLUMNS):
            print(car_park[row][col], end=" ")
        print()  # New line for next row

# Main program
def main():
    # Initialize car park grid
    car_park = [["empty" for _ in range(COLUMNS)] for _ in range(ROWS)]
    empty_car_park(car_park)

    while True:
        # Display menu of options
        print("\n1. Reset all spaces in the car park to 'empty'")
        print("2. Park a car")
        print("3. Remove a car")
        print("4. Display the car park grid")
        print("5. Quit")
        option = input("Enter your choice: ")

        if option == "1":
            empty_car_park(car_park)
        elif option == "2":
            park_a_car(car_park)
        elif option == "3":
            remove_a_car(car_park)
        elif option == "4":
            display_car_park_grid(car_park)
        elif option == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice - please re-enter.")

# Run the main program
if __name__ == "__main__":
    main()
