
class Force_Vector(object):
    '''
    Holds manually defined force-vector
    '''
    def __init__(self, x, y, z):
        '''
        init force-vector
        '''
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
        self.start = None
        self.stop = None
        
    def set_start_stop(self, start, stop):
        '''
        Set start and stop values
        '''
        self.start = start
        self.stop = stop
