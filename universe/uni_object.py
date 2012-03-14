
class Uni_Object(object):
    '''
    This class represents any object in universe
    '''
    
    def __init__(self, name, mass, radius):
        
        self.name = name
        self.mass = float(mass)
        
        self.x = float(0)
        self.y = float(0)
        self.z = float(0)

        self.speed_x = float(0)
        self.speed_y = float(0)
        self.speed_z = float(0)
        
        self.force_vector_list = []
        
        self.radius = float(radius)
        
        self.object_type = 3 # TODO object: Uni_Object_Type
        
        self.color = (255,255,255)

    def set_speed(self, speed_x, speed_y, speed_z):
        
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z
        
    def set_location(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z
        
    def add_force_vector(self, force):
        
        self.force_vector_list.append(force)

    def clear_force_vector_list(self):
        
        self.force_vector_list = []
        
    def set_object_type(self, object_type):
        
        self.object_type = object_type
