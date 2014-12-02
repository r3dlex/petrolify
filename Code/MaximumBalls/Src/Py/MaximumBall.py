from ArrayToRawFile import ArrayToRawFile
from scipy import ndimage
from datetime import datetime

class MaximumBall:
    __img_array = None

    def __init__(self, img):
        self.__img_array = img

    def CalcMaximumBalls(self):
        print "Calcing Maximum Balls"
        spheres_data = self.InflateSpheres()
        self.RemoveSpheres()
        self.CreateHierarchy()

    def InflateSpheres(self):
        print "Inflating spheres"
        time = datetime.now()
        edt, indices = ndimage.morphology.distance_transform_edt(self.__img_array, return_indices=True)
        time = datetime.now() - time
        print "Inflate took " + str(time.total_seconds()) + "s"
        edt_file = ArrayToRawFile(edt, '/tmp/edt_300_300_300.raw')
        edt_file.write_and_close()
        indices_file = ArrayToRawFile(indices, '/tmp/indices_300_300_300.raw')
        indices_file.write_and_close()
        return edt

    def RemoveSpheres(self):
        print "Removing spheres"

    def CreateHierarchy(self):
        print "Creating sphere hierarchy"
