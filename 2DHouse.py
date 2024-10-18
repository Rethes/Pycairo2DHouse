# trapezium begins here
# Set the color for the trapezium (black)
context.set_source_rgb(0, 0, 0)

# Define the trapezium points (shorter base on top, longer base at the bottom)
top_base_width = 1000
bottom_base_width = 1300
height_of_trapezium = 100

# Coordinates for the trapezium
top_left_x = (width - top_base_width) / 2
top_left_y = 980  # Space from the top

bottom_left_x = (width - bottom_base_width) / 2
bottom_left_y = top_left_y + height_of_trapezium

# Draw the trapezium
context.move_to(top_left_x, top_left_y)  # Top left
context.line_to(top_left_x + top_base_width, top_left_y)  # Top right
context.line_to(bottom_left_x + bottom_base_width, bottom_left_y)  # Bottom right
context.line_to(bottom_left_x, bottom_left_y)  # Bottom left
context.close_path()

# Fill the trapezium
context.fill()

# Draw the windows (white rectangles)
window_width = 50
window_height = 50
window_spacing = 20

# Left window
context.set_source_rgb(1, 1, 1)  # Set color to white for windows
context.rectangle(house_x + window_spacing, house_y + window_spacing, window_width, window_height)
context.fill()

# Right window
context.rectangle(house_x + window_spacing * 2 + window_width, house_y + window_spacing, window_width, window_height)
context.fill()