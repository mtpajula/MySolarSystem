
class Force_Vector(object):
    
    def __init__(self, x, y, z):
        
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
        self.start = None
        self.stop = None
        
    def set_start_stop(self, start, stop):
        self.start = start
        self.stop = stop
