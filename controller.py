from universe.universe import Universe
from universe.uni_object import Uni_Object
from universe.force_vector import Force_Vector
from uni_file.dom_save import Dom_Save
from uni_file.dom_load import Dom_Load
import copy

class controller(object):
    
    def __init__(self):
        
        self.universe = Universe()
        #self.universe.maths.set_step(10)
        self.copy_universe = None
        
        self.file_name = "test.xml"
        self.folder = "files/"
    
    def create_object(self, name, mass, radius):
        
        #print "create object:"
        #print "name: " + name
        #print "mass: " + mass
        
        uni_object = Uni_Object(name, mass, radius)
        self.universe.add_object(uni_object)
        
        return uni_object
        
    def create_angle_force(self, uni_object, force, angle2d, angle3d):
        
        ( x, y, z ) = self.universe.maths.get_vector_xyz(force, angle2d, angle3d)
        force = Force_Vector(x, y, z)
        
        uni_object.add_force_vector(force)
        
        return force
        
    def set_object_angle_speed(self, uni_object, speed, angle2d, angle3d):
        
        ( x, y, z ) = self.universe.maths.get_vector_xyz(speed, angle2d, angle3d)
        uni_object.set_speed(x, y, z)
        

    def animate_step(self):
        #print "animate"

        self.universe.move_objects()
        
        
    def animate(self, amount, stepsize, note_step, obj_num):
        '''
        BROKE
        '''
        
        self.universe.maths.time = stepsize
        #self.universe.maths.set_step(stepsize)
        
        x = []
        y = []
        z = []
        
        
        print "amount: " + str(amount) + " stepsize: " + str(stepsize) + " note_step: " + str(note_step)
        
        for i in range(amount):
            
            self.animate_step()
            
            if ( (i+1) % note_step ) == 0:
                print str(self.universe.step) +" x: "+ str(self.universe.object_list[obj_num].x)
                
                x.append(self.universe.object_list[obj_num].x)
                y.append(self.universe.object_list[obj_num].y)
                z.append(self.universe.object_list[obj_num].z)
                
        xyz = [x,y,z]
        
        return xyz
    
    def set_startpoint(self):
        
        self.copy_universe = copy.deepcopy(self.universe)
        
    def reverse_startpoint(self):
        
        if self.copy_universe is not None:
            self.universe = copy.deepcopy(self.copy_universe)
        else:
            print "No saved universe"
        
    def save(self):
        s = Dom_Save()
        s.add_universe(self.universe)
        
        if self.copy_universe is not None:
            s.add_universe(self.copy_universe)
        
        s.save_simulation(self.folder + self.file_name)
        
    def load(self):
        l = Dom_Load()
        uni_list = l.load_simulation(self.folder + self.file_name)
        print uni_list
        
        if len(uni_list) == 1:
            self.universe = uni_list[0]
            self.copy_universe = None
        elif len(uni_list) >= 2:
            self.universe = uni_list[0]
            self.copy_universe = uni_list[1]
        else:
            print "Not enough universe-objects"
        
        
        
