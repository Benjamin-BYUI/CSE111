from tkinter import *
import math
import random

# Change these to change simulation behavior.
NUM_PEOPLE = 50
PEOPLE_RADIUS = 25
CHANCE_CONTRACT = 50
PERCENT_QUARANTINING = 60
TIME_CONTAGIOUS_SECONDS = 5
REFRESH_DELAY = 30

def main():
    """ Sets up tkinter elements and calls functions to begin the drawing process. """
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = Tk()
    root.geometry(f"{width}x{height}")
    root.title("Disease analysis")

    # Create a Frame object.
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1)

    # Begin the drawing process.
    draw_simulation(canvas, 0, 0, width-1, height-1)
    root.mainloop()

def draw_simulation(canvas, left, top, right, bottom):
    """ Initializes the people as circles and calls a looping function to animate them. """
    circles = initialize_circles(canvas, left, top, right, bottom)
    
    # Begin the infinite loop function to move the circles.
    move_circles(canvas, circles, left, top, right, bottom)

def initialize_circles(canvas, left, top, right, bottom):
    """ Initializes the people as circles in the form of a list of dictionaries and returns that list.
        Returns: a list of dictionaries "circles" representing people.
    """
    circles = []
    # try in case the user input constants are invalid.
    try:
        for i in range(int(NUM_PEOPLE)):
            rand_x = random.randrange(left, right - int(PEOPLE_RADIUS) * 2)
            rand_y = random.randrange(top, bottom - int(PEOPLE_RADIUS) * 2)
            circle = canvas.create_oval(rand_x, rand_y, rand_x + int(PEOPLE_RADIUS) * 2, rand_y + int(PEOPLE_RADIUS) * 2, fill="#00FF00")
            circles.append({})
            circles[i]["id"] = circle
            circles[i]["state"] = "well"
            if random.randrange(0, 100) < int(PERCENT_QUARANTINING):
                circles[i]["quarantining"] = True
                circles[i]["delta_x"] = 0
                circles[i]["delta_y"] = 0
            else:
                circles[i]["quarantining"] = False
                circles[i]["delta_x"] = random.randrange(-int(PEOPLE_RADIUS) // 2, int(PEOPLE_RADIUS) // 2)
                circles[i]["delta_y"] = random.randrange(-int(PEOPLE_RADIUS) // 2, int(PEOPLE_RADIUS) // 2)

        # Make one person initially sick
        random_person_index = random.randrange(0, len(circles))
        make_sick(canvas, circles[random_person_index])
    
    except Exception as e:
        print("Please use a number > 0 for NUM_PEOPLE,")
        print("And a number > 0 but < half the width or height for PEOPLE_RADIUS,")
        print("And a number for PERCENT_QUARANTINING.")
        exit()

    return circles

def move_circles(canvas, circles, left, top, right, bottom):
    """ Handles the movement of circles and calls all other functions regarding collision between circles or the border
    of the screen to handles those cases. 
    """
    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            if collision_detection(canvas, circles[i], circles[j]):
                collision_resolution(canvas, circles[i], circles[j])
                contract_resolution(canvas, circles[i], circles[j])
        border_collide = border_collision_detection(canvas, left, top, right, bottom, circles[i])
        if not border_collide == "none":
            border_collision_resolution(border_collide, circles[i])
    
    for circle in circles:
        canvas.move(circle["id"], circle["delta_x"], circle["delta_y"])
    
    # try in case the user input constant is invalid.
    try:
        # Infinitely repeat this function every REFRESH_DELAY.
        canvas.after(int(REFRESH_DELAY), move_circles, canvas, circles, left, top, right, bottom)
    except Exception as e:
        print("Please use a positive number for REFRESH_DELAY.")
        exit()

def collision_detection(canvas, obj1, obj2):
    """ Calculates collision between two circles and returns that result. 
        Return: True if the two circles collide; False if not.
    """
    X2 = 2
    Y2 = 3
    obj1_coords = canvas.coords(obj1["id"])
    obj2_coords = canvas.coords(obj2["id"])
    obj1_center_X = obj1_coords[X2] - int(PEOPLE_RADIUS)
    obj1_center_Y = obj1_coords[Y2] - int(PEOPLE_RADIUS)
    obj2_center_X = obj2_coords[X2] - int(PEOPLE_RADIUS)
    obj2_center_Y = obj2_coords[Y2] - int(PEOPLE_RADIUS)
    distance_apart = math.sqrt( (obj2_center_X - obj1_center_X)**2 + (obj2_center_Y - obj1_center_Y)**2 )
    if distance_apart <= int(PEOPLE_RADIUS) * 2:
        return True
    return False

def collision_resolution(canvas, obj1, obj2):
    """ Resolves the case where two circles collided. Causes these two circles to bounce off each other in
    opposite directions, or for just one to bounce off if the other is quarantining (cannot move.)
    """
    X2 = 2
    Y2 = 3
    obj1_coords = canvas.coords(obj1["id"])
    obj2_coords = canvas.coords(obj2["id"])
    obj1_center_X = obj1_coords[X2] - int(PEOPLE_RADIUS)
    obj1_center_Y = obj1_coords[Y2] - int(PEOPLE_RADIUS)
    obj2_center_X = obj2_coords[X2] - int(PEOPLE_RADIUS)
    obj2_center_Y = obj2_coords[Y2] - int(PEOPLE_RADIUS)
    angle = math.atan2((obj2_center_Y - obj1_center_Y), (obj2_center_X - obj1_center_X))
    obj1_speed = math.sqrt( obj1["delta_x"]**2 + obj1["delta_y"]**2 )
    obj2_speed = math.sqrt( obj2["delta_x"]**2 + obj2["delta_y"]**2 )
    if obj1["quarantining"]:
        obj2["delta_x"] = math.cos(angle) * obj2_speed
        obj2["delta_y"] = math.sin(angle) * obj2_speed
    elif obj2["quarantining"]:
        obj1["delta_x"] = math.cos(angle + math.pi) * obj1_speed
        obj1["delta_y"] = math.sin(angle + math.pi) * obj1_speed
    else:
        obj1["delta_x"] = math.cos(angle + math.pi) * obj2_speed
        obj1["delta_y"] = math.sin(angle + math.pi) * obj2_speed
        obj2["delta_x"] = math.cos(angle) * obj1_speed
        obj2["delta_y"] = math.sin(angle) * obj1_speed
    
def contract_resolution(canvas, obj1, obj2):
    """ Resolves whether the disease contracts when two circles have collided. 
    Calls the make_sick function based on this result.
    """
    # try in case the user input constant is invalid.
    try:
        if obj1["state"] == "well" and obj2["state"] == "sick":
            if random.randrange(0, 100) < int(CHANCE_CONTRACT):
                make_sick(canvas, obj1)
        if obj1["state"] == "sick" and obj2["state"] == "well":
            if random.randrange(0, 100) < int(CHANCE_CONTRACT):
                make_sick(canvas, obj2)
    except Exception as e:
        print("Please use a number for CHANCE_CONTRACT.")
        exit()

def border_collision_detection(canvas, left, top, right, bottom, obj):
    """ Calculates collision between a circle and a screen border and returns that result. 
        Return: The border name ("left", "top", "right", "bottom") if a collision is detected; otherwise "none".
    """
    X1 = 0
    Y1 = 1
    X2 = 2
    Y2 = 3
    obj_coords = canvas.coords(obj["id"])
    if obj_coords[X1] <= left:
        return "left"
    if obj_coords[Y1] <= top:
        return "top"
    if obj_coords[X2] >= right:
        return "right"
    if obj_coords[Y2] >= bottom:
        return "bottom"
    return "none"

def border_collision_resolution(border_collide, obj):
    """ Resolves the case where a circle collided with the border. changes the circle's delta_x or
    delta_y to make it return to the screen based on which border was collided.
    """
    if border_collide == "left":
        obj["delta_x"] = abs(obj["delta_x"])
    if border_collide == "top":
        obj["delta_y"] = abs(obj["delta_y"])
    if border_collide == "right":
        obj["delta_x"] = -abs(obj["delta_x"])
    if border_collide == "bottom":
        obj["delta_y"] = -abs(obj["delta_y"])

def make_sick(canvas, obj):
    """ Causes the circle obj to become sick and relfect that change on the screen visually. 
    Also calls the recover function to make it recover after TIME_CONTAGIOUS_SECONDS.
    """
    # try in case the user input constant is invalid.
    try: 
        obj["state"] = "sick"
        canvas.itemconfig(obj["id"], fill="#FF0000")
        canvas.after(int(float(TIME_CONTAGIOUS_SECONDS) * 1000), recover, canvas, obj)
    except Exception as e:
        print("Please use a number for TIME_CONTAGIOUS_SECONDS.")
        exit()

def recover(canvas, obj):
    """ Causes the circle obj to recover and reflect that state on the screen visually. """
    obj["state"] = "recovered"
    canvas.itemconfig(obj["id"], fill="#FF00FF")

# Begins the program.
if __name__ == "__main__":
    main()