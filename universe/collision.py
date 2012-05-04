import copy

class CollisionManager(object):
    '''
    Class f0r recording collisions
    '''
    def __init__(self, maths):
        
        self.maths = maths
        self.collision_list = []
    
    def record(self, uni_obj1, uni_obj2, time):
        
        collision = Collision(uni_obj1, uni_obj2, time)
        self.maths.collision(collision.alive, collision.deleted)
        self.collision_list.append(collision)
        
        return collision.get_deleted()


class Collision(object):
    '''
    Class for managing and saving collision
    '''
    
    def __init__(self, uni_obj1, uni_obj2, time):
        
        self.uni_obj1 = uni_obj1
        self.uni_obj2 = uni_obj2
        
        self.alive = None
        self.deleted = None
        self.time = time
        
        self.find_larger_mass()
        
    def find_larger_mass(self):
        
        if self.uni_obj1.mass < self.uni_obj2.mass:
            self.alive = self.uni_obj2
            self.deleted = self.uni_obj1
        else:
            self.alive = self.uni_obj1
            self.deleted = self.uni_obj2
            
    def get_deleted(self):
        
        return self.deleted
        
        
        
        
