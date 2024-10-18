import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 300)
ctx = cairo.Context(surface)

# Set background color
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

# Set line width
ctx.set_line_width(2)

# Draw  cross
ctx.move_to(195, 50)
ctx.line_to(195, 15)
ctx.move_to(185, 25)
ctx.line_to(205, 25)
ctx.set_source_rgb(0, 0, 0)
ctx.stroke()
ctx.fill()

# Draw trapezium
ctx.move_to(180, 90)
ctx.line_to(210, 90)
ctx.line_to(200, 50)
ctx.line_to(190, 50)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# Draw triangle above trapezium
ctx.move_to(190, 50)
ctx.line_to(200, 50)
ctx.line_to(195, 40)
ctx.line_to(190, 50)
ctx.fill()

# Draw rectangle below the cross
ctx.rectangle(160, 85, 70, 9)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw left rectangle
ctx.rectangle(50, 220, 100, 40)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

#draw right rectangle
ctx.rectangle(260, 220, 100, 40)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw small rectangles
for x in [60, 90, 280, 310]:
    ctx.rectangle(x, 230, 20, 15)
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

# Draw left trapezium
ctx.move_to(100, 190)
ctx.line_to(130, 190)
ctx.line_to(130, 220)
ctx.line_to(40, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw right trapezium
ctx.move_to(260, 190)
ctx.line_to(310, 190)
ctx.line_to(350, 220)
ctx.line_to(260, 220)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw rectangle at the centre
ctx.move_to(130, 170)
ctx.line_to(130, 270)
ctx.line_to(260, 270)
ctx.line_to(260, 170)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()


# Draw top part of the chapel
ctx.move_to(130, 170)
ctx.line_to(130, 270)
ctx.line_to(260, 270)
ctx.line_to(260, 170)
ctx.line_to(240, 160)
ctx.line_to(150, 160)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw  roof
ctx.move_to(120, 180)
ctx.line_to(150, 160)
ctx.line_to(240, 160)
ctx.line_to(270, 180)
ctx.line_to(270, 170)
ctx.line_to(240, 150)
ctx.line_to(150, 150)
ctx.line_to(120, 170)
ctx.close_path()
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 1)
ctx.stroke()

# Draw circular window
ctx.arc(195, 175, 10, math.radians(0), math.radians(360))
ctx.set_source_rgb(1, 1, 1)
ctx.fill()

# Draw doors
ctx.rectangle(160, 220, 34, 47)
ctx.rectangle(196, 220, 34, 47)
ctx.fill()

# Draw top part of the chapel
ctx.rectangle(170, 100, 50, 50)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.stroke()

# Draw the arch
ctx.move_to(180, 120)
ctx.line_to(180, 147)
ctx.line_to(210, 147)
ctx.line_to(210, 120)
ctx.arc(195, 120, 15, math.pi, 0)
ctx.set_source_rgb(1, 1, 1)
ctx.fill_preserve()
ctx.stroke()


surface.write_to_png('2Dhouse.png')