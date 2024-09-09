# Get user input
hours = int(input("Enter the hours (1-12): "))
minutes = int(input("Enter the minutes (0-59): "))
period = input("Enter AM or PM: ").strip().lower()

# Convert to 24-hour format
if period == 'pm' and hours != 12:
    hours += 12
elif period == 'am' and hours == 12:
    hours = 0

# Calculate total minutes since midnight
total_minutes = hours * 60 + minutes

# Output the result
print(f"The number of minutes since midnight is: {total_minutes}")
