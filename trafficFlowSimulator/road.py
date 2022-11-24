from scipy.spatial import distance  
  
# defining the Road class  
class Road:  
    def __init__(self, start, end):  
        self.start = start  
        self.end = end  
        self.initProperties()  
  
    def initProperties(self):  
        self.length = distance.euclidean(self.start, self.end)  
        self.angleSin = (self.end[1] - self.start[1]) / self.length  
        self.angleCos = (self.end[0] - self.start[0]) / self.length  