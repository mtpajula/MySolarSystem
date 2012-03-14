from maths import Maths


class Universe(object):
    '''
    Universe class has objects in it and it requires maths-object
    '''
    
    def __init__(self):
        
        self.object_list = []
        
        self.maths = Maths()
        
        self.step = 0
    
    def add_object(self, uni_object):
        
        self.object_list.append(uni_object)

    def get_object_list(self):
        
        return self.object_list

    def calculate_gravity(self):
        
        #print "Calculating..."
        
        amount = len(self.object_list)
        
        for i in range(amount):
            
            j = i + 1
            
            for k in range(j, amount):

                #print "\n" + self.object_list[i].name +" + "+self.object_list[k].name
                del_object = self.maths.gravity(self.object_list[i], self.object_list[k])
                
                if del_object is not None:
                    self.object_list.remove(del_object)
                    self.calculate_gravity()
                    return
                
    def move_objects(self):
        
        #print "Moving..."
        
        self.step += 1
        self.calculate_gravity()
        
        for uni_object in self.object_list:
            self.maths.move(uni_object, self.step)
            
        #print self.step
