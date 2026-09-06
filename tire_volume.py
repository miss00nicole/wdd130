import math 
from datetime import datetime
#I added a program that provides prices for common tire size
#Tire information from the user
width = float(input("Enter the width of the tire in mm (ex 205):"))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60):"))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15):"))
print()
#Calculate the tire volume
volume = (math.pi * width**2 * aspect_ratio *
            (width * aspect_ratio + 2540 * diameter))/ 10000000000
#Display the tire volume
print(f"The approximate volume is {volume:.2f}litres") 
#Finding prices for common tire sizes
if width == 185 and aspect_ratio == 50 and diameter == 14:
    price = 52.99
elif width == 205 and aspect_ratio == 60 and diameter == 15:
    price = 58.97
elif width == 215 and aspect_ratio == 65 and diameter == 16:
    price = 69.98
elif width == 225 and aspect_ratio == 65 and diameter == 17:
    price = 79.08
else:
    price = 0
    #Display the tire price
    if price > 0:
        print(f"The price of the the tire is ${price:.2f}")
    else:
        print("A price for this tire size was not found.")
#Get the current date
current_date_and_time = datetime.now()
#Open the volums.txt file for appending
with open ("volume.txt", "at") as volumes_file:
    #write the date, tire information and volume to the file
    print(f"{current_date_and_time:%Y-%m-%d}")
    print(f"{width:g}{aspect_ratio:g},{diameter:g},{volume:2f}")
    files=volumes_file