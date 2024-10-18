import cairo

import cairo

# Set up the image surface and context
width, height = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)

# Set the background color (white)
context.set_source_rgb(1, 1, 1)
context.paint()

# Define the cross properties
cross_thickness = 5  # Thickness of both arms of the cross
cross_length = 35  # Length of each arm (horizontal and vertical)
horizontal_length = 35

# Set the color for the cross (black)
context.set_source_rgb(0, 0, 0)

# Draw the vertical arm of the cross
context.rectangle(
    (width - cross_thickness) / 2,  # X position (centered)
    (height - cross_length) / 2,  # Y position (centered)
    cross_thickness,  # Width of the vertical arm
    cross_length  # Height of the vertical arm
)
context.fill()

# Draw the horizontal arm of the cross
context.rectangle(
    (width - cross_length) / 2,  # X position (centered)
    (height - cross_thickness) / 2,  # Y position (centered)
    # cross_length,  # Width of the horizontal arm
    horizontal_length,  # Width of the horizontal arm (shorter
    cross_thickness  # Height of the horizontal arm
)
context.fill()

# Draw the triangle at the top of the cross
# Move to the top center of the vertical arm
top_of_cross_x = width / 2
top_of_cross_y = (height - cross_length) / 2  # Y position of the top of the vertical arm

# Start at the top center of the cross
context.move_to(top_of_cross_x, top_of_cross_y)

# Define the other two vertices of the triangle above the cross
context.line_to(top_of_cross_x - 75, top_of_cross_y - 100)  # Left point of the triangle
context.line_to(top_of_cross_x + 75, top_of_cross_y - 100)  # Right point of the triangle

# Close the path to form the triangle
context.close_path()

# Fill the triangle with black
context.fill()

# Save the image
surface.write_to_png("output/2DHouse.png")

print("Black filled cross image saved as 2DHouse.png")
