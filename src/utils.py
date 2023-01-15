class Traffic_Signal:
    def __init__(self,red,yellow,green,timer_text):
        self.red = red
        self.yellow = yellow 
        self.green = green 
        self.timer_text = '' #timer_text to display the timer value


class Vehicle(pygame.sprite.Sprite):
    class Vehicle(pygame.sprite.Sprite):
        def __init__(Self,lane,vehicleClass,direction_number,direction,will_turn):
            pygame.sprite.Sprite.__init__(self)
            self.lane = lane 
            self.vehicleClass = vehicleClass 
            self.speed = speed 
            self.direction_number = direction_number
            self.direction = direction
            self.x = x[direction][lane]
            self.y = y[direction][lane]
            self.will_turn = will_turn

            self.turned = 0
            self.rotateAngle = 0
            vehicles[direction][lane].append(self)
            self.crossedIndex = 0
            path = "../images/" + direction + "/" + vehicleClass + ".png"
            self.originalImage = pygame.image.load(path)
            self.image = pygame.image.load(path)

            if (len(vehicles[direction][lane])>1 and vehicles[direction][lane][self.index-1].crossed == 0):
                pass 
