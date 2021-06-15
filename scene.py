import tkinter as tk
import math
import itertools
import random

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    SCENE_WIDTH = scene_right - scene_left + 1
    SCENE_HEIGHT = scene_bottom - scene_top + 1

    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)

    GROUND_Y = 300
    draw_ground(canvas, scene_left, GROUND_Y, scene_right, scene_bottom)

    draw_spiral(canvas, scene_left, scene_top, scene_right, scene_bottom)

    grid_spacing_x = 10
    draw_edge_spiral_grids(canvas, scene_left, scene_top, scene_right, scene_bottom, grid_spacing_x)

    draw_sun(canvas, SCENE_WIDTH, SCENE_HEIGHT)

    LOWEST_CLOUD_Y = GROUND_Y - 50
    FARTHEST_CLOUD_X = SCENE_WIDTH - 100
    NUMBER_OF_CLOUDS = 50
    for cloud in range(NUMBER_OF_CLOUDS):
        cloud_left = scene_left + random.randrange(FARTHEST_CLOUD_X)
        cloud_top = scene_top + random.randrange(LOWEST_CLOUD_Y)

        CLOUD_DISTANCE_FROM_CENTER = math.sqrt((SCENE_WIDTH / 2 - cloud_left) ** 2 + (SCENE_HEIGHT / 2 - cloud_top) ** 2)
        CLOUD_DISTANCE_FROM_CENTER_SIZE_RATIO = CLOUD_DISTANCE_FROM_CENTER / 600
        cloud_size = CLOUD_DISTANCE_FROM_CENTER_SIZE_RATIO
        draw_cloud(canvas, cloud_left, cloud_top, SCENE_WIDTH, SCENE_HEIGHT, cloud_size)


    HIGHEST_TREE_Y = GROUND_Y - 50
    LOWEST_TREE_Y = scene_bottom - 50
    FARTHEST_TREE_X = SCENE_WIDTH - 50
    NUMBER_OF_TREES = 50
    for tree in range(NUMBER_OF_TREES):
        tree_left = scene_left + random.randrange(FARTHEST_TREE_X)
        tree_top = random.randrange(HIGHEST_TREE_Y, LOWEST_TREE_Y)

        TREE_DISTANCE_FROM_CENTER = math.sqrt((SCENE_WIDTH / 2 - tree_left) ** 2 + (SCENE_HEIGHT / 2 - tree_top) ** 2)
        TREE_DISTANCE_FROM_CENTER_SIZE_RATIO = TREE_DISTANCE_FROM_CENTER / 600
        tree_size = TREE_DISTANCE_FROM_CENTER_SIZE_RATIO
        draw_tree(canvas, tree_left, tree_top, SCENE_WIDTH, SCENE_HEIGHT, tree_size)
    
    # grid_spacing = 100
    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, grid_spacing)

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def add_whoosh_lines(canvas, obj_left, obj_top, obj_right, obj_bottom, canvas_width, canvas_height):
    """Draw whoosh lines behind object toward center of screen.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a grid.
        obj_left, obj_top, obj_right, obj_bottom: The x and y location in pixels of the
            top left and bottom right of the object to add whoosh lines to.
        canvas_width, canvas_height: the width and height
            of canvas.
    Return: nothing
    """
    CANVAS_CENTER_X = canvas_width / 2
    CANVAS_CENTER_Y = canvas_height / 2
    OBJ_CENTER_X = obj_right - (obj_right - obj_left) / 2
    OBJ_CENTER_Y = obj_bottom - (obj_bottom - obj_top) / 2
    DELTA_X = CANVAS_CENTER_X - OBJ_CENTER_X
    DELTA_Y = CANVAS_CENTER_Y - OBJ_CENTER_Y
    OBJ_LENGTH_FROM_OBJ_CENTER = math.ceil(math.sqrt((obj_left - OBJ_CENTER_X) ** 2 + (obj_top - OBJ_CENTER_Y) ** 2))
    ANGLE = math.atan2(DELTA_Y, DELTA_X)
    LINE_1_STARTING_X = OBJ_CENTER_X - math.cos(ANGLE) * (1.2 * OBJ_LENGTH_FROM_OBJ_CENTER)
    LINE_1_STARTING_Y = OBJ_CENTER_Y - math.sin(ANGLE) * (1.2 * OBJ_LENGTH_FROM_OBJ_CENTER)
    PERPENDIUCLAR_ANGLE = ANGLE + math.pi / 2
    PARALLEL_LINES_SPACING = OBJ_LENGTH_FROM_OBJ_CENTER / 4
    LINE_2_STARTING_X = LINE_1_STARTING_X + math.cos(PERPENDIUCLAR_ANGLE) * PARALLEL_LINES_SPACING
    LINE_2_STARTING_Y = LINE_1_STARTING_Y + math.sin(PERPENDIUCLAR_ANGLE) * PARALLEL_LINES_SPACING
    LINE_3_STARTING_X = LINE_1_STARTING_X - math.cos(PERPENDIUCLAR_ANGLE) * PARALLEL_LINES_SPACING
    LINE_3_STARTING_Y = LINE_1_STARTING_Y - math.sin(PERPENDIUCLAR_ANGLE) * PARALLEL_LINES_SPACING
    LINE_1_ENDING_X = LINE_1_STARTING_X + math.cos(ANGLE) * OBJ_LENGTH_FROM_OBJ_CENTER
    LINE_1_ENDING_Y = LINE_1_STARTING_Y + math.sin(ANGLE) * OBJ_LENGTH_FROM_OBJ_CENTER
    LINE_2_ENDING_X = LINE_2_STARTING_X + math.cos(ANGLE) * OBJ_LENGTH_FROM_OBJ_CENTER
    LINE_2_ENDING_Y = LINE_2_STARTING_Y + math.sin(ANGLE) * OBJ_LENGTH_FROM_OBJ_CENTER
    LINE_3_ENDING_X = LINE_3_STARTING_X + math.cos(ANGLE) * OBJ_LENGTH_FROM_OBJ_CENTER
    LINE_3_ENDING_Y = LINE_3_STARTING_Y + math.sin(ANGLE) * OBJ_LENGTH_FROM_OBJ_CENTER

    canvas.create_line(LINE_1_STARTING_X, LINE_1_STARTING_Y, LINE_1_ENDING_X, LINE_1_ENDING_Y)
    canvas.create_line(LINE_2_STARTING_X, LINE_2_STARTING_Y, LINE_2_ENDING_X, LINE_2_ENDING_Y)
    canvas.create_line(LINE_3_STARTING_X, LINE_3_STARTING_Y, LINE_3_ENDING_X, LINE_3_ENDING_Y)

def draw_tree(canvas, left, top, canvas_width, canvas_height, size = 1):
    """Draw a tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a grid.
        left, top: The x and y location in pixels of the
            top left of the tree starting location.
        canvas_width, canvas_height: the width and height
            of canvas, used for calling add_whoosh_lines()
        size: Size multiplier of the tree, default = 1
    Return: nothing
    """
    TREE_WIDTH = 100 * size
    TREE_HEIGHT = 200 * size
    TREE_TRUNK_X = left + TREE_WIDTH / 3
    TREE_TRUNK_Y = top + TREE_HEIGHT / 2
    TREE_TRUNK_WIDTH = TREE_WIDTH / 3
    TREE_TRUNK_HEIGHT = TREE_HEIGHT / 2
    TREE_LEAVES_WIDTH = TREE_WIDTH
    TREE_LEAVES_HEIGHT = TREE_HEIGHT / 2

    canvas.create_rectangle(TREE_TRUNK_X, TREE_TRUNK_Y, TREE_TRUNK_X + TREE_TRUNK_WIDTH, TREE_TRUNK_Y + TREE_TRUNK_HEIGHT, fill = "#966F33", width = 0)
    canvas.create_oval(left, top, left + TREE_LEAVES_WIDTH, top + TREE_LEAVES_HEIGHT, fill = "#228b22", width = 0)
    
    add_whoosh_lines(canvas, left, top, left + TREE_WIDTH, top + TREE_HEIGHT, canvas_width, canvas_height)

def draw_sun(canvas, canvas_width, canvas_height):
    """Draw background sun.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a grid.
        canvas_width, canvas_height: the width and height
            of canvas, used for calling add_whoosh_lines()
    Return: nothing
    """
    SUN_X = 650
    SUN_Y = 25
    SUN_WIDTH = 100
    SUN_HEIGHT = 100
    canvas.create_oval(SUN_X, SUN_Y, SUN_X + SUN_WIDTH, SUN_Y + SUN_HEIGHT, fill = "#f9d71c", width = 0)

    add_whoosh_lines(canvas, SUN_X, SUN_Y, SUN_X + SUN_WIDTH, SUN_Y + SUN_HEIGHT, canvas_width, canvas_height)

def draw_sky(canvas, left, top, right, bottom):
    """Draw background sky.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a grid.
        left, top, right, bottom: The x and y location in pixels of the
            top left and bottom right of the canvas.
    Return: nothing
    """
    canvas.create_rectangle(left, top, right, bottom, fill = "#4ec8ed", width = 0)

def draw_ground(canvas, left, top, right, bottom):
    """Draw a ground.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a grid.
        left, top, right, bottom: The x and y location in pixels of the
            top left and bottom right of the ground.
    Return: nothing
    """
    canvas.create_rectangle(left, top, right, bottom, fill = "#34b526", width = 0)

def draw_spiral(canvas, left, top, right, bottom):
    """Draw background vortex spiral.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a grid.
        left, top, right, bottom: The x and y location in pixels of the
            top left and bottom right of the canvas.
    Return: nothing
    """
    RAY_LENGTH_INCREMENTS = 1
    CENTER_X = (right - left + 1) / 2
    CENTER_Y = (bottom - top + 1) / 2
    MAX_DISTANCE_FROM_CENTER = math.ceil(math.sqrt(CENTER_X ** 2 + CENTER_Y ** 2))
    ANGLE_INCREMENTS = (16 * (math.pi / 180))
    
    previous_x = CENTER_X
    previous_y = CENTER_Y
    rainbow_colors = itertools.cycle(["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#8B00FF"])
    current_angle = 0

    # Increment through ray distances from center, chaning angle and drawing color changing rainbow lines
    for ray_length in range (RAY_LENGTH_INCREMENTS, MAX_DISTANCE_FROM_CENTER, RAY_LENGTH_INCREMENTS):
        current_angle = current_angle + ANGLE_INCREMENTS
        current_x = CENTER_X + math.cos(current_angle) * ray_length
        current_y = CENTER_Y + math.sin(current_angle) * ray_length
        current_color = next(rainbow_colors)
        canvas.create_line(previous_x, previous_y, current_x, current_y, fill = current_color, width = 5)

        previous_x = current_x
        previous_y = current_y

def draw_edge_spiral_grids(canvas, left, top, right, bottom, grid_spacing):
    """Draw background vortex spiral.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a grid.
        left, top, right, bottom: The x and y location in pixels of the
            top left and bottom right of the canvas.
        grid_spacing: Space in pixels between spiral grid lines.
    Return: nothing
    """
    CENTER_X = int((right - left + 1) / 2)
    CENTER_Y = int((bottom - top + 1) / 2)
    WIDTH_HEIGHT_RATIO = CENTER_Y / CENTER_X

    rainbow_colors = itertools.cycle(["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#8B00FF"])

    # Draw top left grid
    for x in range(grid_spacing, CENTER_X, grid_spacing):
        color = next(rainbow_colors)
        canvas.create_line(x, top, left, CENTER_Y - x * WIDTH_HEIGHT_RATIO, fill = color, width = 2)
    
    # Draw bottom left grid
    for x in range(grid_spacing, CENTER_X, grid_spacing):
        color = next(rainbow_colors)
        canvas.create_line(x, bottom, left, CENTER_Y + x * WIDTH_HEIGHT_RATIO, fill = color, width = 2)

    # Draw top right grid
    for x in range(right - grid_spacing, CENTER_X, -grid_spacing):
        color = next(rainbow_colors)
        canvas.create_line(x, top, right, CENTER_Y + (x - right) * WIDTH_HEIGHT_RATIO, fill = color, width = 2)
    
    # Draw bottom right grid
    for x in range(right - grid_spacing, CENTER_X, -grid_spacing):
        color = next(rainbow_colors)
        canvas.create_line(x, bottom, right, CENTER_Y - (x - right) * WIDTH_HEIGHT_RATIO, fill = color, width = 2)
    
    # # Draw grid columns
    # for x in range(scene_left, scene_right, grid_spacing):
    #     canvas.create_line(x, scene_top, x, scene_bottom)
    #     canvas.create_text(x + text_margin, scene_top + text_margin, text = x)

def draw_cloud(canvas, left, top, canvas_width, canvas_height, size = 1):
    """Draw a cloud.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a grid.
        left, top: The x and y location in pixels of the
            top left of the cloud starting location.
        canvas_width, canvas_height: the width and height
            of canvas, used for calling add_whoosh_lines()
        size: Size multiplier of the cloud, default = 1
    Return: nothing
    """
    CLOUD_WIDTH = 200 * size
    CLOUD_HEIGHT = 100 * size
    CLOUD_OVAL_WIDTH = CLOUD_WIDTH * (1 / 2)
    CLOUD_OVAL_HEIGHT = CLOUD_HEIGHT * (2 / 3)
    CLOUD_OVAL_1_X = left
    CLOUD_OVAL_1_Y = top + CLOUD_HEIGHT / 3
    CLOUD_OVAL_2_X = left + CLOUD_WIDTH / 2
    CLOUD_OVAL_2_Y = CLOUD_OVAL_1_Y
    CLOUD_OVAL_3_X = (CLOUD_OVAL_1_X + CLOUD_OVAL_2_X) / 2
    CLOUD_OVAL_3_Y = top
    CLOUD_OVAL_4_X = CLOUD_OVAL_3_X
    CLOUD_OVAL_4_Y = CLOUD_OVAL_1_Y

    canvas.create_oval(CLOUD_OVAL_1_X, CLOUD_OVAL_1_Y, CLOUD_OVAL_1_X + CLOUD_OVAL_WIDTH, CLOUD_OVAL_1_Y + CLOUD_OVAL_HEIGHT, fill = "#fff", width = 0)
    canvas.create_oval(CLOUD_OVAL_2_X, CLOUD_OVAL_2_Y, CLOUD_OVAL_2_X + CLOUD_OVAL_WIDTH, CLOUD_OVAL_2_Y + CLOUD_OVAL_HEIGHT, fill = "#fff", width = 0)
    canvas.create_oval(CLOUD_OVAL_3_X, CLOUD_OVAL_3_Y, CLOUD_OVAL_3_X + CLOUD_OVAL_WIDTH, CLOUD_OVAL_3_Y + CLOUD_OVAL_HEIGHT, fill = "#fff", width = 0)
    canvas.create_oval(CLOUD_OVAL_4_X, CLOUD_OVAL_4_Y, CLOUD_OVAL_4_X + CLOUD_OVAL_WIDTH, CLOUD_OVAL_4_Y + CLOUD_OVAL_HEIGHT, fill = "#fff", width = 0)

    add_whoosh_lines(canvas, left, top, left + CLOUD_WIDTH, top + CLOUD_HEIGHT, canvas_width, canvas_height)

# def draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, grid_spacing):
#     """Draw a grid.
#     Parameters
#         canvas: The tkinter canvas where this
#             function will draw a grid.
#         scene_left, scene_top: The x and y location in pixels of the
#             top left canvas location.
#         scene_right, scene_bottom: The x and y location in pixels of the
#             bottom right canvas location.
#         grid_spacing: Space in pixels between grid lines.
#     Return: nothing
#     """
#     TEXT_MARGIN = 12

#     # Draw grid rows
#     for y in range(scene_top, scene_bottom, grid_spacing):
#         canvas.create_line(scene_left, y, scene_right, y)
#         canvas.create_text(scene_left + TEXT_MARGIN, y + TEXT_MARGIN, text = y)
    
#     # Draw grid columns
#     for x in range(scene_left, scene_right, grid_spacing):
#         canvas.create_line(x, scene_top, x, scene_bottom)
#         canvas.create_text(x + TEXT_MARGIN, scene_top + TEXT_MARGIN, text = x)

# Call the main function so that
# this program will start executing.
main()