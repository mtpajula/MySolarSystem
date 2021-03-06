from maths import Maths
from collision import CollisionManager

class Universe(object):
    '''
    Universe class has objects in it and it requires maths-object
    '''
    
    def __init__(self):
        
        self.object_list = []
        
        self.maths = Maths()
        self.collision_manager = CollisionManager(self.maths)
        
        self.step = 0
        self.calc_time = 0
    
    def add_object(self, uni_object):
        '''
        Appends Object to the object list
        '''
        
        self.object_list.append(uni_object)

    def get_object_list(self):
        '''
        Returns Object list
        '''
        
        return self.object_list

    def calculate_gravity(self):
        '''
        Calculates new values to Object's force vectors
        By the law of gravity
        
        It goes through each object pair.
        '''
        
        amount = len(self.object_list)
        
        for i in range(amount):
            
            j = i + 1
            
            for k in range(j, amount):

                #print "\n" + self.object_list[i].name +" + "+self.object_list[k].name
                collision = self.maths.gravity(self.object_list[i], self.object_list[k])
                '''
                if del_object is not None:
                    self.object_list.remove(del_object)
                    self.calculate_gravity()
                    return
                '''
                if collision:
                    del_object = self.collision_manager.record(self.object_list[i], self.object_list[k], self.calc_time)
                    self.object_list.remove(del_object)
                    #self.calculate_gravity()
                    return
                
    def move_objects(self):
        '''
        Moves each object based on it's force vector(s)
        '''
        for uni_object in self.object_list:
            uni_object.clear_force()
        
        self.step += 1
        self.calc_time += self.maths.time
        self.calculate_gravity()
        
        for uni_object in self.object_list:
            self.maths.move(uni_object, self.calc_time)
            
            
