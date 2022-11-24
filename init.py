from .road import *  
from .simulator import *  
from .window import *  

def __init__(self,config={}):
    #We are going to set the default configuration
    self.set_default_config()

     # Updating the configuration  
    for attr, val in config.items():  
        setattr(self, attr, val)  