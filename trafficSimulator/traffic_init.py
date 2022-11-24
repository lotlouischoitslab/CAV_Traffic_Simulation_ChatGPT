def __init__(self, config = {}):  
    # Setting the default configuration  
    self.set_default_config()  
  
    # Updating the configuration  
    for attr, val in config.items():  
        setattr(self, attr, val)  