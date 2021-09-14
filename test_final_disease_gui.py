from final_disease_gui import initialize_circles, move_circles, collision_detection, collision_resolution, \
    border_collision_detection, border_collision_resolution, make_sick, recover
import pytest
from tkinter import *
import math

width = 800
height = 500

# Create the Tk root object.
root = Tk()
root.geometry(f"{width}x{height}")
root.title("Disease analysis")

# Create a Frame object.
frame = Frame(root)

# Create a canvas object that will draw into the frame.
canvas = Canvas(frame)

left = 0
right = width - 1
top = 0
bottom = height - 1


def test_initialize_circles():
    circles_dict = initialize_circles(canvas, left, top, right, bottom)
    assert len(circles_dict) > 0
    circle_keys = circles_dict[0].keys()
    assert "id" in circle_keys
    assert "state" in circle_keys
    assert "quarantining" in circle_keys
    assert "delta_x" in circle_keys
    assert "delta_y" in circle_keys

def test_move_circles():
    circles_test = []
    circle = canvas.create_oval(5, 5, 15, 15)
    circle_obj = {}
    circle_obj["id"] = circle
    circle_obj["delta_x"] = 0
    circle_obj["delta_y"] = 0
    circles_test.append(circle_obj)

    circle2 = canvas.create_oval(300, 300, 310, 310)
    circle2_obj = {}
    circle2_obj["id"] = circle2
    circle2_obj["delta_x"] = 5
    circle2_obj["delta_y"] = 3
    circles_test.append(circle2_obj)

    move_circles(canvas, circles_test, left, top, right, bottom)
    assert canvas.coords(circles_test[0]["id"]) == [5.0, 5.0, 15.0, 15.0]
    assert canvas.coords(circles_test[1]["id"]) == [305.0, 303.0, 315.0, 313.0]
    circle2_obj["delta_x"] = 20
    circle2_obj["delta_y"] = 30
    move_circles(canvas, circles_test, left, top, right, bottom)
    assert canvas.coords(circles_test[0]["id"]) == [5.0, 5.0, 15.0, 15.0]
    assert canvas.coords(circles_test[1]["id"]) == [325.0, 333.0, 335.0, 343.0]

def test_collision_detection():
    circle = canvas.create_oval(5, 5, 15, 15)
    circle_obj = {}
    circle_obj["id"] = circle

    circle2 = canvas.create_oval(10, 10, 20, 20)
    circle2_obj = {}
    circle2_obj["id"] = circle2

    assert collision_detection(canvas, circle_obj, circle2_obj)
    not_colliding_circle = canvas.create_oval(300, 300, 310, 310)
    circle2_obj["id"] = not_colliding_circle
    assert not collision_detection(canvas, circle_obj, circle2_obj)

def test_collision_resolution():
    circle = canvas.create_oval(5, 5, 15, 15)
    circle_obj = {}
    circle_obj["id"] = circle
    circle_obj["quarantining"] = True
    circle_obj["delta_x"] = 0
    circle_obj["delta_y"] = 0

    circle2 = canvas.create_oval(10, 10, 20, 20)
    circle2_obj = {}
    circle2_obj["id"] = circle2
    circle2_obj["quarantining"] = False
    circle2_obj["delta_x"] = 5
    circle2_obj["delta_y"] = 3

    circle_obj_center_X = 10
    circle_obj_center_Y = 10
    circle2_obj_center_X = 15
    circle2_obj_center_Y = 15
    circle2_obj_speed = math.sqrt( circle2_obj["delta_x"]**2 + circle2_obj["delta_y"]**2 )
    angle = math.atan2((circle2_obj_center_Y - circle_obj_center_Y), (circle2_obj_center_X - circle_obj_center_X))
    collision_resolution(canvas, circle_obj, circle2_obj)
    assert circle2_obj["delta_x"] == math.cos(angle) * circle2_obj_speed
    assert circle2_obj["delta_y"] == math.sin(angle) * circle2_obj_speed

    circle_obj["quarantining"] = False
    circle2_obj["quarantining"] = True
    circle_obj_speed = math.sqrt( circle_obj["delta_x"]**2 + circle_obj["delta_y"]**2 )
    collision_resolution(canvas, circle_obj, circle2_obj)
    assert circle_obj["delta_x"] == math.cos(angle + math.pi) * circle_obj_speed
    assert circle_obj["delta_y"] == math.sin(angle + math.pi) * circle_obj_speed

    circle_obj["quarantining"] = False
    circle2_obj["quarantining"] = False
    circle_obj_speed = math.sqrt( circle_obj["delta_x"]**2 + circle_obj["delta_y"]**2 )
    circle2_obj_speed = math.sqrt( circle2_obj["delta_x"]**2 + circle2_obj["delta_y"]**2 )
    collision_resolution(canvas, circle_obj, circle2_obj)
    assert circle_obj["delta_x"] == math.cos(angle + math.pi) * circle2_obj_speed
    assert circle_obj["delta_y"] == math.sin(angle + math.pi) * circle2_obj_speed
    assert circle2_obj["delta_x"] == math.cos(angle) * circle_obj_speed
    assert circle2_obj["delta_y"] == math.sin(angle) * circle_obj_speed

def test_border_collision_detection():
    circle = canvas.create_oval(5, 5, 15, 15)
    obj = {}
    obj["id"] = circle
    assert border_collision_detection(canvas, left, top, right, bottom, obj) == "none"

    circle = canvas.create_oval(left - 5, 5, 15, 15)
    obj = {}
    obj["id"] = circle
    assert border_collision_detection(canvas, left, top, right, bottom, obj) == "left"

    circle = canvas.create_oval(5, top - 5, 15, 15)
    obj = {}
    obj["id"] = circle
    assert border_collision_detection(canvas, left, top, right, bottom, obj) == "top"

    circle = canvas.create_oval(5, 5, right + 5, 15)
    obj = {}
    obj["id"] = circle
    assert border_collision_detection(canvas, left, top, right, bottom, obj) == "right"

    circle = canvas.create_oval(5, 5, 15, bottom + 5)
    obj = {}
    obj["id"] = circle
    assert border_collision_detection(canvas, left, top, right, bottom, obj) == "bottom"

def test_border_collision_resolution():
    circle = canvas.create_oval(left - 5, 5, 15, 15)
    obj = {}
    obj["id"] = circle
    obj["delta_x"] = -5
    border_collision_resolution("left", obj)
    assert obj["delta_x"] == 5

    circle = canvas.create_oval(5, top - 5, 15, 15)
    obj = {}
    obj["id"] = circle
    obj["delta_y"] = -5
    border_collision_resolution("top", obj)
    assert obj["delta_y"] == 5

    circle = canvas.create_oval(5, 5, right + 5, 15)
    obj = {}
    obj["id"] = circle
    obj["delta_x"] = 5
    border_collision_resolution("right", obj)
    assert obj["delta_x"] == -5

    circle = canvas.create_oval(5, 5, 15, bottom + 5)
    obj = {}
    obj["id"] = circle
    obj["delta_y"] = 5
    border_collision_resolution("bottom", obj)
    assert obj["delta_y"] == -5

def test_make_sick():
    circle = canvas.create_oval(5, 5, 15, 15, fill="#00FF00")
    circle_obj = {}
    circle_obj["id"] = circle
    circle_obj["state"] = "well"

    make_sick(canvas, circle_obj)
    assert circle_obj["state"] == "sick"
    assert canvas.itemcget(circle, "fill") == "#FF0000"

def test_recover():
    circle = canvas.create_oval(5, 5, 15, 15, fill="#FF0000")
    circle_obj = {}
    circle_obj["id"] = circle
    circle_obj["state"] = "sick"

    recover(canvas, circle_obj)
    assert circle_obj["state"] == "recovered"
    assert canvas.itemcget(circle, "fill") == "#FF00FF"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_final_disease_gui.py"])