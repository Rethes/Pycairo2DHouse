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


# Set up the surface and context
width, height = 500, 600  # Adjust dimensions for the shape
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

# Set background color to white
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Set drawing color to black
ctx.set_source_rgb(0, 0, 0)

# Draw the top rectangle (smaller rectangle at the top)
top_rect_width = 300
top_rect_height = 40
ctx.rectangle((width - top_rect_width) / 2, 50, top_rect_width, top_rect_height)
ctx.fill()

# Draw the large bottom rectangle (the main body)
bottom_rect_width = 400
bottom_rect_height = 350
ctx.rectangle((width - bottom_rect_width) / 2, 150, bottom_rect_width, bottom_rect_height)
ctx.fill()

# Draw the arch (arched window in the center)
arch_width = 150
arch_height = 220
center_x, center_y = width // 2, 300

# Draw the bottom part of the arched window (rectangle part)
ctx.rectangle(center_x - arch_width // 2, center_y, arch_width, arch_height // 2)
ctx.set_source_rgb(1, 1, 1)  # White fill for the window
ctx.fill()

# Draw the top curved part of the arched window (half-circle)
ctx.arc(center_x, center_y, arch_width // 2, 3.14, 0)  # Half-circle (upper part of the arch)
ctx.fill()

# Fill the pedestal
ctx.fill()

# Save the image to a file
surface.write_to_png("church.png")
