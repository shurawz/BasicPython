
# Example of turtle module ((((Approach 1))))
#
# import time
# import turtle
# # Here, turtle is the module that is to imported to make the code executed.
#
# turtle.forward(150)
# turtle.right(250)
# turtle.forward(150)
#
# time.sleep(4)

# Example of turtle module ((((Approach 2))))

# from turtle import forward, right, done
#
# #Since forward, right and done functions are already called so it isnot necessary to recall them in the further program.
#
# forward(150)
# right(250)
# forward(150)
#
# done() # When done() is called from turtle module, It stops the PYTHON TURTLE GRAPHICS and we can close it on our way.


# Some additional ideas on above topic is:

from turtle import *

forward(150)
right(250)
circle(74)
forward(150)

done()

# The 'turtle graphics' opens, runs, automatically it gets closed in any part of the code where there is problem.
