import math
import numpy.random as rand
from scipy.stats import lognorm
import sys, os

def getHandler(a, b, c, d):
    return math.sqrt(a + b + c + d)

def postHandler():
    return "POST MEAN SQUARE"

def putHandler():
    return "PUT MEAN SQUARE"

def deleteHandler():
    return "DELETE MEAN SQUARE"
