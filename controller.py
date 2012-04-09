from universe.universe import Universe
from universe.uni_object import Uni_Object
from universe.force_vector import Force_Vector
from uni_file.dom_save import Dom_Save
from uni_file.dom_load import Dom_Load
import copy
import os

class controller(object):
    '''
    Controlls universe
    '''
    
    def __init__(self):
        '''
        init new universe
        '''
        self.universe = Universe()
        
        # Holds the startpoint universe
        self.copy_universe = None
        
        # Folder where to save files and Default file name
        self.file_name = "test.xml"
        self.folder = "files/"
        
        # AU in meters for UI:s
        self.au = 149598000000
    
    def create_object(self, name, mass, radius):
        '''
        Creates Object and adds it to the current universe
        '''
        uni_object = Uni_Object(name, mass, radius)
        self.universe.add_object(uni_object)
        
        return uni_object
        
    def create_angle_force(self, uni_object, force, angle2d, angle3d):
        '''
        Creates force vector from force and it's angles
        force,angle_xy,angle,xz => x,y,z (starting from the object location)
        '''
        
        ( x, y, z ) = self.universe.maths.get_vector_xyz(force, angle2d, angle3d)
        force = Force_Vector(x, y, z)
        
        uni_object.add_force_vector(force)
        
        return force
        
    def set_object_angle_speed(self, uni_object, speed, angle2d, angle3d):
        '''
        Sets object speed vector by transforming
        speed,angle_xy,angle,xz => x,y,z (starting from the object location)
        '''
        
        ( x, y, z ) = self.universe.maths.get_vector_xyz(speed, angle2d, angle3d)
        uni_object.set_speed(x, y, z)
        
    def get_object_angle_speed(self, uni_object):
        '''
        Get speed vector in angle form
        '''
        return self.universe.maths.xyz_to_angle(uni_object.x, uni_object.y, uni_object.z)

    def animate_step(self):
        '''
        Simulates universe ba one step
        '''

        self.universe.move_objects()
        
    
    def animate(self, obj_num, time):
        '''
        Simulation is executed one year and it returns x-axis values divided by
        initial x-axis value from given object per month.
        
        Also step size is needed
        '''
        

        running = True
        
        self.universe.maths.time = time
        
        status, message = self.set_startpoint()
        
        hour = round(3600.0 / self.universe.maths.time)
        day = round(hour*24.0)
        month = round(day*30.0)
        year = round(day*365.0)
        run_day = 0
        
        message += "\n============="
        
        while running:
            
            if (self.universe.step % day) == 0:
                run_day += 1
                os.system("clear")
                print str(round((100 * self.universe.step / year),2)) + " % "
            
            if (self.universe.step % month) == 0:
                #print "month: " + str(self.controller.universe.step)
                x = self.universe.object_list[obj_num].x / self.copy_universe.object_list[obj_num].x
                x = str(x).replace(".",",")
                message += "\n" + x
            
            if self.universe.step > year:
                running = False
            
            self.animate_step()
            
        message += "\n============="
            
        if status is True:
            message += "\nSimulation done. x-position monthly, over a year"
        return status, message
    
    def set_startpoint(self):
        '''
        Sets startpoint for universe. It copies current in 
        copy_universe
        '''
        
        self.copy_universe = copy.deepcopy(self.universe)
        
        return True, "Startpoint set"
        
    def reverse_startpoint(self):
        '''
        Copies startpoint-universe as the current one.
        If no startpoint-universe is set, then nothing is done.
        '''
        
        if self.copy_universe is not None:
            self.universe = copy.deepcopy(self.copy_universe)
            return True, "Startpoint reversed"
        
        return False, "No saved universe"
        
    def save(self):
        '''
        Saves current simulation in file
        '''
        s = Dom_Save()
        s.add_universe(self.universe)
        
        if self.copy_universe is not None:
            s.add_universe(self.copy_universe)
        
        return s.save_simulation(self.folder + self.file_name)
        
    def load(self):
        '''
        Loads simulation from file
        '''
        l = Dom_Load()
        uni_list = l.load_simulation(self.folder + self.file_name)
        
        if uni_list is not None:
            
            if len(uni_list) == 1:
                self.universe = uni_list[0]
                self.copy_universe = None
            elif len(uni_list) >= 2:
                self.universe = uni_list[0]
                self.copy_universe = uni_list[1]
            else:
                return False, "Not enough universe-objects"
            return True, "Ok"
                
        return False, "File not found"
            
    def list_files_in_folder(self):
        '''
        Returns files from file-folder
        '''
        
        files = []
        for f in os.listdir(self.folder):
            files.append(f)
            
        return files
        
