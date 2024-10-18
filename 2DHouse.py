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
