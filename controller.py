from universe.universe import Universe
from universe.uni_object import Uni_Object

class controller(object):
    
    def __init__(self):
        
        self.universe = Universe()
    
    def create_object(self, name, mass):
        
        print "create object:"
        print "name: " + name
        print "mass: " + mass
        
        uni_object = Uni_Object(name, mass)
        self.universe.add_object(uni_object)
        

    def print_info(self):
        print "info"

    def animate(self):
        print "animate"
        
        print self.universe.get_object_list()
        
