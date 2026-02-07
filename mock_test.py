from graphix import Window, Point, Line, Circle, Rectangle, Text


def the_painter():
    win = Window("The painter", 320, 240)

    # Stick figure
    head = Circle(Point(100, 60), 20)
    head.draw(win)

    body = Line(Point(100, 80), Point(100, 130))
    body.draw(win)

    arm_l = Line(Point(100, 90), Point(70, 100))
    arm_l.draw(win)

    arm_r = Line(Point(100, 90), Point(135, 95))
    arm_r.draw(win)

    leg_l = Line(Point(100, 130), Point(80, 180))
    leg_l.draw(win)

    leg_r = Line(Point(100, 130), Point(120, 180))
    leg_r.draw(win)

    brush_tip = Point(150, 90)
    brush = Line(Point(135, 95), brush_tip)
    brush.fill_colour = "brown"
    brush.outline_colour = "brown"
    brush.outline_width = 3
    brush.draw(win)

    drop_radius = 3
    drop = Circle(
        Point(brush_tip.x, brush_tip.y + brush.outline_width // 2 + drop_radius),
        drop_radius,
    )
    drop.fill_colour = "blue"
    drop.draw(win)

    bucket = Rectangle(Point(140, 160), Point(190, 190))
    bucket.fill_colour = "grey"
    bucket.outline_colour = "black"
    bucket.draw(win)

    text = Text(Point(150, 40), "")
    text.draw(win)

    for char in "Drip!":
        win.get_mouse()
        text.text += char
        drop.move(0, 12)

    win.get_mouse()
    drop.undraw()

    win.get_mouse()
    win.close()


if __name__ == "__main__":
    the_painter()
