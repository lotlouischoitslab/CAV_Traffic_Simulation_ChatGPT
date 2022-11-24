# importing the Road class  
from .road import Road  
  
# defining the Simulator class  
class Simulator:  
    def __init__(self, config = {}):  
        # Setting default configuration  
        self.set_default_config()  
  
        # Updating configuration  
        for attr, val in config.items():  
            setattr(self, attr, val)  
  
    def set_default_config(self):  
        # Time keeping  
        self.t = 0.0  
        # Frame count keeping  
        self.frame_count = 0  
        # Simulation time step  
        self.dt = 1/60  
        # Array to store roads  
        self.roads = []  
  
    def createRoad(self, start, end):  
        the_road = Road(start, end)  
        self.roads.append(the_road)  
        return the_road  
  
    def createRoads(self, roadList):  
        for the_road in roadList:  
            self.createRoad(*the_road)  