print('Drawing an outdoor scene by Innocent Hove. \nDrawing of the the sky, clouds, fog, sun, \ntrees with fruit on and on the ground, mountains, and a dam.')
import tkinter as tk
import math

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
    # print(scene_left, scene_top, scene_right, scene_bottom)
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
    
    draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 20)
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 350
    hill_center = scene_left + 100
    hill_top = scene_top + 200
    hill_height = 280
    draw_sky(canvas, 0, 0)
    draw_sun(canvas, 660, 10)
    draw_cloud(canvas, 80, 40, scale=1.2)
    draw_cloud(canvas, 135, 5)
    draw_cloud(canvas, 185, 25, scale=.9)
    draw_cloud(canvas, 275, 10)
    draw_cloud(canvas, 5, 5, scale=1.2)
    draw_cloud(canvas, 400, 100)
    draw_cloud(canvas, 500, 60, scale=1.1)
    draw_ground(canvas, 0, 280)
    draw_hill(canvas, hill_center - 70, hill_top - 60, hill_height + 140)
    draw_hill(canvas, hill_center, hill_top, hill_height)
    draw_hill(canvas, hill_center + 90, hill_top, hill_height + 30)
    draw_fog(canvas, 50, 200)
    draw_fog(canvas, 10, 195)
    draw_fog(canvas, 30, 210)
    draw_fog(canvas, 2, 250, scale=1.5)
    draw_tree(canvas, tree_center + 100, tree_top - 50, tree_height + 30, scale = .9)
    draw_tree(canvas, tree_center, tree_top, tree_height)
    draw_tree(canvas, tree_center - 100, tree_top + 50, tree_height - 30, scale = 1.1)
    draw_fruit(canvas, 500, 200)
    draw_fruit(canvas, 460, 250)
    draw_fruit(canvas, 560, 280)
    draw_fruit(canvas, 540, 350)
    draw_fruit(canvas, 485, 195)
    draw_fruit(canvas, 600, 240)
    draw_fruit(canvas, 415, 270)
    draw_fruit(canvas, 380, 330)
    draw_fruit(canvas, 460, 350)
    draw_fruit(canvas, 470, 450)
    draw_fruit(canvas, 430, 430)
    draw_fruit(canvas, 570, 440)
    draw_fruit(canvas, 420, 470)
    draw_pond(canvas, -80, 330)
    draw_pond(canvas, -55, 295)
  
def draw_sky(canvas, x, y):
    """Draw the sky.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the sky.
        x, y: The x and y location in pixels where
            this function will draw the top left.
    Return: nothing
    """
    x = 0
    y = 0
    x1 = 800
    y1 =280
    canvas.create_rectangle(x, y, x1, y1, width = False, fill = "#00FFFF")

def draw_ground(canvas, x, y):
    """Draw the ground.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the ground.
        x, y: The x and y location in pixels where
            this function will draw the top left.
    Return: nothing
    """
    x = 0
    y = 280
    x1 = 800
    y1 =500
    canvas.create_rectangle(x, y, x1, y1, width = False, fill = "#556B2F")

def draw_sun(canvas, sun_left, sun_top):
    """Draw the sun.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the sun.
        sun_left, sun_top: The x and y location in pixels where
            this function will draw the top left of the sun.
    Return: nothing
    """
    sun_width = 100
    sun_height = 100
    ray_length = 100
    ray_width = 3
    ray_count = 15
    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)
    
    
    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill = '#FFF7B4', width = False)
    # loop to divide the whole circle at a given angle
    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length

        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width = ray_width, fill='#FFF7B4')

def draw_cloud(canvas, cloud_left, cloud_top, scale=1):
    """Draw the a single cloud.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the cloud.
        cloud_left, cloud_top: The x and y location in pixels where
            this function will draw the top left of the cloud.
    Return: nothing
    """
    cloud_width = 150 * scale
    cloud_height = 100 * scale
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height

    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill = '#FFFAFA', width = False)

def draw_pond(canvas, pond_left, pond_top):
    """Draw the a pond.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the pond.
        pond_left, pond_top: The x and y location in pixels where
            this function will draw the top left of the pond.
    Return: nothing
    """
    pond_width = 150
    pond_height = 90
    
    pond_right = pond_left + pond_width
    pond_bottom = pond_top + pond_height

    canvas.create_oval(pond_left, pond_top, pond_right, pond_bottom, fill = '#00FFFF', width = False)

def draw_fog(canvas, fog_left, fog_top, scale=1):
    """Draw the fog.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the fog.
        fog_left, fog_top: The x and y location in pixels where
            this function will draw the top left of the fog.
    Return: nothing
    """
    fog_width = 150 * scale
    fog_height = 5 * scale
    
    fog_right = fog_left + fog_width
    fog_bottom = fog_top + fog_height

    canvas.create_oval(fog_left, fog_top, fog_right, fog_bottom, fill = '#A9A9A9', width = False)

def draw_fruit(canvas, fruit_left, fruit_top, scale=1):
    """Draw a fruit.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the fruit.
        fruit_left, fruit_top: The x and y location in pixels where
            this function will draw the top left of the fruit.
    Return: nothing
    """
    fruit_width = 5 * scale
    fruit_height = 5 * scale
    
    fruit_right = fruit_left + fruit_width
    fruit_bottom = fruit_top + fruit_height

    canvas.create_oval(fruit_left, fruit_top, fruit_right, fruit_bottom, fill = '#DC143C', width = False)

def draw_grid(canvas, top, left, right, bottom, grid_spacing):
    """The drawing grid
    Parameters
        canvas: The tkinter canvas where this
            function will draw the fruit.
        top, left, right. bottom: The drawing space in the drawing canvas where grid lines will be added.
    Return: nothing
    """
    # Write grid labels
    text_horizontal_margin = 10
    text_vertical_margin = 5
    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f'{i}')
    
    # Draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_horizontal_margin, text=f'{i}')
    


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_tree(canvas, peak_x, peak_y, height, scale = 1):
    """Draw a single tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a tree.
        height: The height in pixels of the tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10 * scale
    trunk_height = height / 2.5 * scale
    trunk_left = peak_x - trunk_width / 2 * scale
    trunk_right = peak_x + trunk_width / 2 * scale
    trunk_bottom = peak_y + height * scale

    skirt_width = height / 2 * scale
    skirt_height = (height - trunk_height) * 1.25  * scale
    skirt_left = peak_x - skirt_width / 2 * scale
    skirt_right = peak_x + skirt_width / 2 * scale
    skirt_bottom = peak_y + skirt_height * scale

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=False, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=False, fill="dark green")

def draw_hill(canvas, peak_x, peak_y, height):
    """Draw a single hill.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a hill.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a hill.
        height: The height in pixels of the hill that
            this function will draw.
    Return: nothing
    """

    skirt_width = height / 1.5
    skirt_height = height / 3
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the crown (also called skirt) of the hill.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom, width=False, fill="#183D2D")

# Call the main function so that
# this program will start executing.
main()