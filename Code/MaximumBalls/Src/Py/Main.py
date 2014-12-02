#!/usr/bin/env python

from MaximumBall import  MaximumBall

import sys
import numpy

def main():
    if len(sys.argv) > 4:
        filepath = sys.argv[1]
        try:
            dimx = int(sys.argv[2])
        except:
            print "Could not convert dimx"
        try:
            dimy = int(sys.argv[3])
        except:
            print "Could not convert dimy"
        try:
            dimz = int(sys.argv[4])
        except:
            print "Could not convert dimz"
        read_data = numpy.fromfile(filepath, dtype=numpy.uint8)
        read_data = numpy.reshape(read_data, (dimz, dimy, dimx))
        maximum_ball = MaximumBall(read_data)
        maximum_ball.CalcMaximumBalls()
    else:
        print "Usage: PROGRAM Filepath DimX DimY DimZ"

main()
