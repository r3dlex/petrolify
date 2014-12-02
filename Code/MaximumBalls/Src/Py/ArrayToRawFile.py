import numpy

class ArrayToRawFile:
    __array = None
    __filepath = None

    def __init__(self, array, filepath):
        self.__array = array
        self.__filepath = filepath

    def write_and_close(self):
        self.__array.tofile(self.__filepath)

