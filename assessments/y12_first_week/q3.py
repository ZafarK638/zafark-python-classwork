# Get the number of minutes since midnight
total_minutes = int(input("Enter the number of minutes since midnight: "))

# Calculate hours and minutes
hours = total_minutes // 60  # Integer division to get hours
minutes = total_minutes % 60  # Remainder gives minutes

# Format hours and minutes to ensure two digits
time_display = f"{hours:02}:{minutes:02}"

# Output the time in digital clock format
print(f"The time is: {time_display}")
