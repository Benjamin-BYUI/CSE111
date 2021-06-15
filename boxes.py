import math

items_num = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

print(f"For {items_num} items, packing {items_per_box} items in each box, "
f"you will need {math.ceil(items_num / items_per_box)} boxes.")