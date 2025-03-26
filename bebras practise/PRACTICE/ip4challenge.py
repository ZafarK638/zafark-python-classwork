ip_address = input()
valid_ip_address = True
valid_characters = "0123456789."
pointcount = 0
for i in ip_address:
    if i not in valid_characters:
        valid_ip_address = False
    if i == ".":
        pointcount +=1
if pointcount != 3:
    valid_ip_address = False
if valid_ip_address == True:
    ipnum = [int(n) for n in ip_address.split(".")]
    for num in ipnum:
        if ((num < 0) or (num > 255)):
            valid_ip_address = False
if valid_ip_address == True:
    print("Valid IP address")
else:
    print("Invalid IP address")