from trafficFlowSimulator import *  
  
# Creating simulation  
firstSimulation = Simulator()  
  
# Adding one road  
firstSimulation.createRoad((300, 97), (0, 97))  
  
# Adding multiple roads  
firstSimulation.createRoads([  
    ((300, 97), (0, 97)),  
    ((0, 101), (300, 101)),  
    ((180, 61), (0, 61)),  
    ((220, 56), (180, 61)),  
    ((300, 31), (220, 56)),  
    ((180, 61), (160, 97)),  
    ((158, 131), (300, 131)),  
    ((0, 179), (300, 179)),  
    ((300, 181), (0, 181)),  
    ((160, 101), (156, 180))  
      
])  
  
# Starting the simulation  
firstWindow = Window(firstSimulation)  
firstWindow.loop()  