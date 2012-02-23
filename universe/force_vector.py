
class force_vector(object):
    
    def __init__(self, force, angle2d, angle3d):
        
        self.force = force
        self.angle2d = angle2d
        self.angle3d = angle3d
        
        self.start = None
        self.stop = None
    
    def set_start(self, start):
        
        self.start = start
        
    def set_stop(self, stop):
        
        self.stop = stop
