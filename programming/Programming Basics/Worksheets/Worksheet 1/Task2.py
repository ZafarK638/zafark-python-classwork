print("This program assumes that all doors and windows have the same dimensions")



# entering the dimensions of the room
room_height = float(input("Please enter the height of the room in metres: "))
room_width = float(input("Please enter the width of the room in metres: "))
room_length = float(input("Please enter the length of the room in metres: "))
room_surface_area = (room_height * room_width * 2) + (room_width * room_length * 2) + (room_length * room_height * 2)

# entering the dimensions of the unpaintable areas
unpaint_dim = float(input("Please enter the total area of the parts of the room that you don't want painted, e.g. doors, windows: "))

# calculating the area needed to be painted
paint_area = float(room_surface_area - unpaint_dim)

#calculating the amount of paint needed
paint = float(paint_area/11)

print("You will need ", paint, " litres of paint.")