import cairo
import math

# Set up the surface and context
width, height = 1500, 1500  # Adjust height to make room for the full shape
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Set background color to white
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Set the drawing color to black
ctx.set_source_rgb(0, 0, 0)

# Define the center for the cross and the dimensions
center_x, center_y = width // 2, 150  # Center point for the cross
cross_width, cross_height = 40, 120   # Width of arms and height of the vertical bar of the cross

# Draw vertical rectangle for the cross
ctx.rectangle(center_x - cross_width // 4, center_y - cross_height // 2, cross_width // 2, cross_height)

# Draw horizontal rectangle for the cross
ctx.rectangle(center_x - cross_width // 2, center_y - cross_width // 4, cross_width, cross_width // 2)

# Fill the cross
ctx.fill()

# Define points for the pedestal (tapered trapezoid)
pedestal_top_width = 50
pedestal_bottom_width = 150
pedestal_height = 320
pedestal_top_y = center_y + cross_height // 2  # Start the pedestal below the cross

# Draw the pedestal (trapezoid)
ctx.move_to(center_x - pedestal_top_width // 2, pedestal_top_y)   # Top left
ctx.line_to(center_x + pedestal_top_width // 2, pedestal_top_y)   # Top right
ctx.line_to(center_x + pedestal_bottom_width // 2, pedestal_top_y + pedestal_height)  # Bottom right
ctx.line_to(center_x - pedestal_bottom_width // 2, pedestal_top_y + pedestal_height)  # Bottom left
ctx.close_path()

# Draw the top rectangle (smaller rectangle at the top)
top_rect_width = 500
top_rect_height = 40
ctx.rectangle((width - top_rect_width) / 2, 550, top_rect_width, top_rect_height)
ctx.fill()

# Draw the large bottom rectangle (the main body)
bottom_rect_width = 400
bottom_rect_height = 350
ctx.rectangle((width - bottom_rect_width) / 2, 600, bottom_rect_width, bottom_rect_height)
ctx.fill()

# Draw the arch (arched window in the center)
arch_width = 150
arch_height = 220
center_x, center_y = width // 2, 800

# Draw the bottom part of the arched window (rectangle part)
ctx.rectangle(center_x - arch_width // 2, center_y, arch_width, arch_height // 2)
ctx.set_source_rgb(1, 1, 1)  # White fill for the window
ctx.fill()

# Draw the top curved part of the arched window (half-circle)
ctx.arc(center_x, center_y, arch_width // 2, 3.14, 0)  # Half-circle (upper part of the arch)
ctx.fill()

# Fill the pedestal
ctx.fill()

# Define the points for the trapezium
x0, y0 = 150, 150  # Top-left point
x1, y1 = 40, 150  # Top-right point
x2, y2 = 400, 350  # Bottom-right point
x3, y3 = 100, 350  # Bottom-left point

# Start drawing the trapezium
ctx.move_to(x0, y0)  # Move to top-left point
ctx.line_to(x1, y1)  # Draw line to top-right point
ctx.line_to(x2, y2)  # Draw line to bottom-right point
ctx.line_to(x3, y3)  # Draw line to bottom-left point
ctx.close_path()     # Close the shape (connect to top-left)


# Fill the trapezium
ctx.fill()

# Optionally, you can stroke the outline of the trapezium
ctx.set_line_width(2)
ctx.set_source_rgb(0, 0, 0)  # Outline color
ctx.stroke()

# here is the bottom

# Set the color for the house and roof (black)
ctx.set_source_rgb(0, 0, 0)

# Draw the house body (rectangle)
house_x = 100
house_y = 1000
house_width = 1300
house_height = 150
ctx.rectangle(house_x, house_y, house_width, house_height)
ctx.fill()

# Draw the roof (triangle)
# ctx.move_to(house_x, house_y)  # Bottom-left corner of the roof (top of the house)
# ctx.line_to(house_x + house_width, house_y)  # Bottom-right corner of the roof
# ctx.line_to(house_x + house_width / 2, house_y - 100)  # Top vertex of the roof
# ctx.close_path()  # Close the triangle path
# ctx.fill()

# Draw the windows (white rectangles)
window_width = 50
window_height = 50
window_spacing = 20

# Left window
ctx.set_source_rgb(1, 1, 1)  # Set color to white for windows
ctx.rectangle(house_x + window_spacing, house_y + window_spacing, window_width, window_height)
ctx.fill()

# Right window
ctx.rectangle(house_x + window_spacing * 2 + window_width, house_y + window_spacing, window_width, window_height)
ctx.fill()

# 3. Draw the left side building (small rectangle)
# side_building_width = 100
# side_building_height = 100
# ctx.rectangle(house_x - side_building_width, house_y + house_height - side_building_height, side_building_width, side_building_height)
# ctx.fill()
#
# # Right side windows
# ctx.rectangle(house_x + house_width + window_spacing, house_y + house_height - side_building_height + window_spacing, window_width, window_height)
# ctx.fill()
# ctx.rectangle(house_x + house_width + 2 * window_spacing + window_width, house_y + house_height - side_building_height + window_spacing, window_width, window_height)
# ctx.fill()

# Save the image to a file
surface.write_to_png("church.png")
