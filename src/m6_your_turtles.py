"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Parker Jordan.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.tracer(2)
im_gonna_screw_this_up = rg.SimpleTurtle('turtle')
im_gonna_screw_this_up.pen = rg.Pen('orange', 5)

size = 50
for k in range(10):
    im_gonna_screw_this_up.draw_circle(size)
    im_gonna_screw_this_up.pen_up()
    im_gonna_screw_this_up.right(45)
    im_gonna_screw_this_up.forward(10)
    im_gonna_screw_this_up.left(45)
    im_gonna_screw_this_up.pen_down()
    size = size - 5

holy_cow_that_actually_worked = rg.SimpleTurtle('turtle')
holy_cow_that_actually_worked.pen = rg.Pen('yellow', 5)

for k in range(200):
    holy_cow_that_actually_worked.right(50)
    holy_cow_that_actually_worked.forward(k)

# Ok... that was pretty cool