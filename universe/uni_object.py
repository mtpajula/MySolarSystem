

class Uni_Object(object):
    
    def __init__(self, name, mass):
        
        self.name = name
        self.mass = mass
        
        self.x = 0
        self.y = 0
        self.z = 0
        
        self.speed = 0
        self.angle2d = 0
        self.angle3d = 0
        
        self.force_vector_list = []
    
    def set_speed(self, speed, angle2d, angle3d):
        
        self.speed = speed
        self.angle2d = angle2d
        self.angle3d = angle3d
        
    def add_force_vector(self, force):
        
        self.force_vector_list.append(force)

    def get_force_vector_list(self):
        
        return self.force_vector_list
