order_value = float(input("Please input the total cost of your order: "))
extra_value = 0.0
ndd = str(input("Do you want to pay £5.00 extra for guaranteed next day delivery? Type 'y' for Yes. Type anything else for no: "))
if order_value < 15.0:
    extra_value = extra_value + 3.5
if ndd == "y":
    extra_value = extra_value + 5.0
final_value = order_value + extra_value
print("Your postal charge is",extra_value," and your final charge is",final_value,".")