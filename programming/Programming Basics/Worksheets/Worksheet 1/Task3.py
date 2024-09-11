# car mileage + total number of litres in tank
car_mileage_last_fillage = float(input("What was the car's mileage the last time it was filled?"))
car_mileage_current = float(input("What is the car's mileage now?"))
total_litres = float(input("What is the total number of litres needed to fill the tank?"))
car_mileage = float(car_mileage_current + car_mileage_last_fillage)
total_gallons = total_litres * 4.546
print(total_gallons)
