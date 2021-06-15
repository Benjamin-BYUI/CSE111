import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000

print()
print(f"The approximate volume is {volume:.1f} cubic cm.")
print()

buy_tires = False
buy_tires_query = ""
while buy_tires_query not in list(["yes", "no"]):
    buy_tires_query = input("Would you like to buy tires with the dimensions entered (yes/no)? ")

if buy_tires_query == "yes":
    buy_tires = True
    phone_number = input("Enter a phone number: ")

from datetime import datetime
current_date_and_time = datetime.now()

with open("volumes.txt", "at") as f:
    if buy_tires:
        print(f"{current_date_and_time.year}-{current_date_and_time.month:02d}-{current_date_and_time.day:02d}, "
        f"{width}, {aspect_ratio}, {diameter}, {volume:.1f}, {phone_number}", file=f)
    else:
        print(f"{current_date_and_time.year}-{current_date_and_time.month:02d}-{current_date_and_time.day:02d}, "
        f"{width}, {aspect_ratio}, {diameter}, {volume:.1f}", file=f)