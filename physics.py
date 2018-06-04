import math as ma
import numpy as np

##################################################################################
#This python library contains any physics equarions that will be needed to deal  #
#with the physics involved in the code.  These equations assume that the device  #
#is uding a spring cannon to launch the object.  These functions assum the theta #
#downward direction is negative                                                  #
#                                                                                #
#- All units in metric units (lengths in meters, mass in grams)                  #
##################################################################################

"""
*target1 = (1,1)
*target2 = (6,1)
*¥ = machine
*initialize at x = 6 --> x = 0

    TABLE (8 ft x 4 ft):
    **every 2 dashes = 1 foot**

       0  1  2  3  4  5  6  7

  0   [-, -, -, -, -, -, -, -]
  1   [-, O, -, -, -, -, O, -]
  2   [-, -, -, -, -, -, -, -]
  3   [-, -, -, -, -, -, -, -]
  4   [-, -, -, -, -, -, -, -]
  5   [-, -, -, -, -, -, -, -]
  6   [-, -, -, -, -, -, -, -]
  7   [-, -, -, -, -, -, -, -]
  -------------------------------
      [-, -, -, -, -, -, -, -]
      [-, -, -, -, -, -, -, -]
      [-, -, -, -, -, -, -, -]
      [-, -, -, -, -, -, -, -]
      [-, -, -, -, -, -, -, -]
      [-, -, -, -, -, -, -, -]
      [-, O, -, -, -, -, O, -]
      [-, -, -, -, -, -, -, -]

                         ¥

  (1,1) = target1 ==> y = 8+(8-1); x = 1
  (6,1) = target2 ==> y = 8+(8-1); x = 6

  given (xx, yy) --> y = 8+(8-yy); x = xx
  theta = arctan(x/y)"""

"""create board"""
board = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

"""helper functions"""
def is_sink(x, y):
    return board[y][x] == 1

def board_to_real(x, y):
    return x, 8 + (8 - y) + 2

def square(n):
    return n * n

def feet_to_metric(l):
    return l * 0.3048

def inch_to_metric(l):
    return l * 0.0254

def theta_x(x, y):
    assert ma.fabs(x) >= 0 and ma.fabs(x) <= 7 and ma.fabs(y) >= 0 and ma.fabs(y) <= 7
    x, y = board_to_real(x, y)
    theta = ma.atan(x/y)
    print(90-(ma.atan(x/y)*180/ma.pi))
    return (ma.pi/2) - ma.atan(x/y)

def distance(x, y):
    return ma.sqrt(square(x) + square(y))

"""kinematics equations *IN METRIC UNITS*"""
