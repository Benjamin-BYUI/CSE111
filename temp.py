from math import remainder
import random
import textwrap
import itertools

x = {}

print(type(x))

for i in range(100):
    fruit = random.choice(["apple", "orange", "mango", "banana", "maracuja"])
    print(fruit)


rainbow_colors = itertools.cycle(["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#8B00FF"])
for i in range(10):
    current_color = next(rainbow_colors)
    print(current_color)