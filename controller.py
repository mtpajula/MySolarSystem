from universe.universe import Universe
from universe.uni_object import Uni_Object
from universe.force_vector import Force_Vector
from uni_file.dom_save import Dom_Save
from uni_file.dom_load import Dom_Load
from units import Units
import copy
import os

class controller(object):
    '''
    Controlls universe
    '''
    
    def __init__(self):
        
        self.new_controller()
        
    def new_controller(self):
        
        self.universe = Universe()
        
        # Holds the startpoint universe
        self.copy_universe = None
        
        # Folder where to save files and Default file name
        self.file_name = "test.xml"
        self.folder = "files/"
        self.filePath = None
        
        self.units = Units()
        
        self.pref_dict = {}
        
        self.timer_time = 10
        self.steps_between_paint = 1
        
    
    def create_object(self, name, mass, radius):
        '''
        Creates Object and adds it to the current universe
        '''
        uni_object = Uni_Object(name, mass, radius)
        self.universe.add_object(uni_object)
        
        return uni_object
        
    def delete_force(self, uni_object, delete_force_vector):
        '''
        delete force from object
        '''
        
        for i, force_vector in enumerate(uni_object.force_vector_list):
            if delete_force_vector == force_vector:
                
                uni_object.force_vector_list.pop(i)
                
                return True, 'Force removed'
        
        return False, 'Force not found'
        
    def delete_object(self, delete_uni_object):
        '''
        delete object from universe
        '''
        
        for i, uni_object in enumerate(self.universe.object_list):
            if delete_uni_object == uni_object:
                
                self.universe.object_list.pop(i)
                
                return True, 'Object removed'
        
        return False, 'Object not found'
        
    def validate_input(self, input_type, text, no_null = False):
        '''
        If input text is invalid, returns default value
        '''
        
        if input_type == 'string':
            
            if text == "":
                text =  'NONAME'
            
        elif input_type == 'int':
            
            if self.is_int(text):
                text =  int(text)
                
                if no_null:
                    if text == 0:
                        text = 1
            else:
                if no_null:
                    text = 1
                else:
                    text = 0
            
        elif input_type == 'float':
            
            if self.is_float(text):
                text =  float(text)
                
                if no_null:
                    if text == 0:
                        text = 1.1
            else:
                if no_null:
                    text = 1.0
                else:
                    text = 0.0
        
        return text
        
    def is_int(self, s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
            
    def is_float(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        
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
        
    def set_force_angle(self, force_vector, force, angle2d, angle3d):
        '''
        Sets force vector by transforming
        speed,angle_xy,angle,xz => x,y,z (starting from the object location)
        '''
        
        ( x, y, z ) = self.universe.maths.get_vector_xyz(force, angle2d, angle3d)
        force_vector.set_force(x, y, z)
        
    def get_object_angle_speed(self, uni_object):
        '''
        Get speed vector in angle form
        '''
        return self.universe.maths.xyz_to_angle(uni_object.speed_x, uni_object.speed_y, uni_object.speed_z)
        
    def get_object_force_speed(self, uni_object):
        '''
        Get object force vector in angle form
        '''
        return self.universe.maths.xyz_to_angle(uni_object.force_x, uni_object.force_y, uni_object.force_z)
    
    def get_force_angle(self, force_vector):
        '''
        Get force vector in angle form
        '''
        return self.universe.maths.xyz_to_angle(force_vector.x, force_vector.y, force_vector.z)
    
    def animate_step(self):
        '''
        Simulates universe one step
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
        
        self.copy_universe.step = 0
        self.copy_universe.calc_time = 0
        
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
        
    def set_filePath(self, filePath):
        '''
        For Qt filepath load/save
        '''
        self.filePath = filePath
        
    def save(self):
        '''
        Saves current simulation in file
        '''
        self.pref_dict['paint'] = {'timer_time' : self.timer_time,
                                    'steps_between_paint' : self.steps_between_paint } 
        
        self.pref_dict['units'] = self.units.save_units()
        s = Dom_Save(self.pref_dict)
        
        s.add_universe(self.universe)
        if  self.copy_universe is not None:
            s.add_universe(self.copy_universe)
        
        if self.filePath is None:
            return s.save_simulation(self.folder + self.file_name)
            
        return s.save_simulation(self.filePath)
        
        
    def load(self):
        '''
        Loads simulation from file
        '''
        l = Dom_Load()
        
        if self.filePath is None:
            filePath = self.folder + self.file_name
        else:
            filePath = self.filePath
        
        (uni_list, self.pref_dict) = l.load_simulation(filePath)
        
        if 'units' in self.pref_dict:
            self.units.load_units(self.pref_dict['units'])
            
        if 'paint' in self.pref_dict:
            self.timer_time = int(self.pref_dict['paint']['timer_time'])
            self.steps_between_paint = int(self.pref_dict['paint']['steps_between_paint'])
        
        if uni_list is not None:
            
            if len(uni_list) == 1:
                self.universe = uni_list[0]
                self.copy_universe = None
            elif len(uni_list) >= 2:
                self.universe = uni_list[0]
                self.copy_universe = uni_list[1]
            else:
                return False, "Not enough universe-objects"
            return True, "Load ok"
                
        return False, "File not found"
            
    def list_files_in_folder(self):
        '''
        Returns files from file-folder
        '''
        
        files = []
        for f in os.listdir(self.folder):
            files.append(f)
            
        return files
        
    def not_empty(self):
        
        if len(self.universe.object_list) > 0:
            return True
        return False
