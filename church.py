import cairo
import math

# Set up the surface and context
width, height = 500, 700  # Adjust height to make room for the full shape
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
pedestal_top_width = 80
pedestal_bottom_width = 200
pedestal_height = 400
pedestal_top_y = center_y + cross_height // 2  # Start the pedestal below the cross

# Draw the pedestal (trapezoid)
ctx.move_to(center_x - pedestal_top_width // 2, pedestal_top_y)   # Top left
ctx.line_to(center_x + pedestal_top_width // 2, pedestal_top_y)   # Top right
ctx.line_to(center_x + pedestal_bottom_width // 2, pedestal_top_y + pedestal_height)  # Bottom right
ctx.line_to(center_x - pedestal_bottom_width // 2, pedestal_top_y + pedestal_height)  # Bottom left
ctx.close_path()

# Fill the pedestal
ctx.fill()

# Save the image to a file
surface.write_to_png("church.png")
