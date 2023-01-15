import pygame

def main():
    defaultGreen = {
        0:9, 
        1:3,
        2:9,
        3:3
    }

    defaultYellow = 2.5 
    defaultRed = 24

    #signals 
    signals = []
    currentGreen = 0

    #number of signals 
    noOfsignals = 4

    nextGreen = (currentGreen+1)%noOfsignals 

    vehicleTypes = {0:'car'}
    speeds = {'car':3}

    # Coordinates of signal image, timer
    signalCoods = [(400, 430), (690, 110), (970, 305), (690, 610)]
    signalTimerCoods = [(450, 480), (760, 160), (1020, 355), (740, 660)]

    # assigning the legs start from the right hand and go ccw 
    directionNumbers = {0:'right' , 1:'down', 2:'left', 3:'up'}

    # coordinate of stop lines and default stop line -> stop before pedestrian crosse line
    # define the stop line by x-coordinate  for right and left and the y-coordinate for up and down
    stopLines = {"right": 350, "down": 197, "left": 1050, "up": 603}
    defaultStop = {"right": 340, "down": 187, "left": 1060, "up": 610}

    # determine the vehicle start from where to where
    x = {'right':[0,0,0], 'down':[755,727,697], 'left':[1400,1400,1400], 'up':[602,627,657]}   
    y = {'right':[348,370,398], 'down':[0,0,0], 'left':[498,466,436], 'up':[800,800,800]}

    vehicles = {'right': {0:[], 1:[], 2:[], 'crossed':0}, 'down': {0:[], 1:[], 2:[], 'crossed':0}, 'left': {0:[], 1:[], 2:[], 'crossed':0}, 'up': {0:[], 1:[], 2:[], 'crossed':0}}
    vehicleTypes = {0:'car'}

    # gap between vehicls (moving and stoping gap)
    moving_gap = 25
    stoping_gap = 25

    # for move() method
    vehiclesTurned = {
        "right": {1: [], 2: []},
        "down": {1: [], 2: []},
        "left": {1: [], 2: []},
        "up": {1: [], 2: []},
    }
    vehiclesNotTurned = {
        "right": {1: [], 2: []},
        "down": {1: [], 2: []},
        "left": {1: [], 2: []},
        "up": {1: [], 2: []},
    }

    rotationAngle = 3  # rotate & drifting facrtor; 2 or 3 is best to have smooth rotation
    mid = {
        "right": {"x": 560, "y": 465},
        "down": {"x": 560, "y": 310},
        "left": {"x": 860, "y": 310},
        "up": {"x": 815, "y": 495},
    }
    # set random or default green signal time here 
    # if you decide to make a simulation for a randomly green time make it True else if you want your simulation to be based on a pre-defined default green time assign it to False
    randomGreenSignalTimer = False
    # set random green signal time range here
    randomGreenSignalTimerRange = [10, 20]
    pygame.init()
    simulation = pygame.sprite.Group()


if __name__ == '__main__':
    main()