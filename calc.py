import math
import numpy.random as rand
from scipy.stats import lognorm
import sys, os

def getHandler():
    return math.sqrt(75)

def postHandler():
    return "POST MEAN SQUARE"

def putHandler():
    return "PUT MEAN SQUARE"

def deleteHandler():
    return "DELETE MEAN SQUARE"
