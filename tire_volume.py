import math

width = 0
aspectRatio = 0
diameter = 0

formatOrIndividual = ""
while formatOrIndividual not in list(["format","individual"]):
    formatOrIndividual = input("Would you like to input the tire dimensions in standard US format (ex \"205/60R15\") or input the values individually? (Type \"format\" or \"individual\"): ").lower()

if formatOrIndividual == "individual":
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspectRatio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
else:
    while True:
        formatted = input("Insert width, aspect ratio, and diameter in standard US format (ex \"205/60R15\"): ").upper()
        try:
            width, aspectAndDiameter = formatted.split("/")
            aspectRatio, diameter = aspectAndDiameter.split("R")
            width = int(width)
            aspectRatio = int(aspectRatio)
            diameter = int(diameter)
        except:
            print("Invalid input. Please ensure the format is correct exactly as shown in the example.")
            continue
        break

volume = (math.pi * width**2 * aspectRatio * (width * aspectRatio + 2540 * diameter)) / 10000000

print()
print(f"The approximate volume is {volume:.1f} cubic cm.")