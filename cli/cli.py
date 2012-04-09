import os

class Cli_Main(object):
    '''
    MySolarSystem CLI
    '''
    
    def __init__(self, controller):
        '''
        Ui for given controller-object
        '''
        self.controller = controller

    def print_help(self):
        
        print "My Solar System Command list:"
        print " - quit \t\t Leave program"
        print " - play \t\t Simulate one step forward"
        print " - pygame \t\t Simulation in pygame window"
        print " - new object \t\t create new object"
        print " - list objects \t List objects in current universe"
        print " - set \t\t\t Set current situation as a startpoint"
        print " - reverse \t\t Reverse back to startpoint"
        print " - xplay \t\t Simulate x-axis changes monthly in one year"
        print " - save [FILE] \t\t Save simulation in file"
        print " - load [FILE] \t\t Load simulation from file"
        print " - files \t\t List files in save-folder"
        print " - edit \t\t Edit object"
        print " - help \t\t Print available command-list"
        
    def menu(self):
        '''
        Start function for CLI
        Prints help and asks for command
        '''
        quit_cli = False
        
        self.print_help()
        
        print "\n"
        
        while quit_cli is False:
            
            command = raw_input('Command?\n')
            
            if command == "quit":
                print "bye!"
                quit_cli = True
            
            elif command == "play":
                self.play()
                
            elif command == "pygame":
                self.pygame()
                
            elif command == "new object":
                self.new_uni_object()
                
            elif command == "list objects":
                self.list_uni_objects()
                
            elif command == "set":
                self.set_copy_universe()
                
            elif command == "reverse":
                self.reverse_universe()
                
            elif command == "help":
                self.print_help()
                
            elif command == "xplay":
                self.x_play()
                
            elif command.startswith("save"):
                self.cli_save(command)
                
            elif command.startswith("load"):
                self.cli_load(command)
                
            elif command == "files":
                self.files()
                
            elif command == "edit":
                self.edit_uni_object()
                
            else:
                print "Unknown command.\n"
                self.print_help()
                
            print "\n"
            
    
    def play(self):
        
        self.controller.animate_step()
        
    def pygame(self):
        
        from cli_pygame import Cli_Pygame
        
        game = Cli_Pygame(self.controller)
        game.start_animation()
        
        
    def edit_uni_object(self):
        self.list_uni_objects()
        obj_num = int(raw_input('Object number?\n'))
        
        self.new_uni_object(obj_num)
        
    def new_uni_object(self, obj_num = None):
        
        if obj_num is not None:
            new_obj = self.controller.universe.object_list[obj_num]
            print new_obj.name +" Mass: "+ str(new_obj.mass) +" Radius: "+ str(new_obj.radius)
        
        name = raw_input('name?\n')
        mass = float(raw_input('mass * 10^21(kg)?\n')) * 10**21
        radius = float(raw_input('radius (m)?\n'))
        
        if obj_num is None:
            new_obj = self.controller.create_object(name, mass, radius)
        else:
            print "xyz:"
            print new_obj.x/self.controller.au
            print new_obj.y/self.controller.au
            print new_obj.z/self.controller.au
        
        print "Location (au):"
        x = float(raw_input('x?\n'))
        y = float(raw_input('y?\n'))
        z = float(raw_input('z?\n'))
        
        x = x * self.controller.au
        y = y * self.controller.au
        z = z * self.controller.au
        
        print "Initial speed vector:"
        
        if obj_num is not None:
            (speed, angle2d, angle3d) = self.controller.get_object_angle_speed(new_obj)
            print "speed: "+ str(speed) +" angle2d: "+ str(angle2d) +" angle3d: "+ str(angle3d)
        
        speed = float(raw_input('speed (m/s)?\n'))
        if speed > 0:
            angle2d = float(raw_input('angle2d (degrees)?\n'))
            angle3d = float(raw_input('angle3d (degrees)?\n'))
            self.controller.set_object_angle_speed(new_obj,speed,angle2d,angle3d)
        
        print "Pygame style:"
        
        if obj_num is not None:
            (r,g,b) = new_obj.color
            print "size: "+ str(new_obj.object_type) +" r: "+ str(r) +" g: "+ str(g) +" b: "+ str(b)
        
        obj_type = int(raw_input('Object size(int)?\n'))
        
        print "Color:"
        r = int(raw_input('Red (0-255)?\n'))
        g = int(raw_input('Green (0-255)?\n'))
        b = int(raw_input('Blue (0-255)?\n'))
        
        new_obj.set_location(x,y,z)
        new_obj.set_object_type(obj_type)
        new_obj.color = (r,g,b)
        
        print "done"
        
    def list_uni_objects(self):
        
        print "step: " + str(self.controller.universe.step)
        print "Name : mass,radius : x,y,z : speed_x,speed_y,speed_z"
        
        for i, uni_object in enumerate(self.controller.universe.get_object_list()):
            print "["+ str(i) +"]"+ uni_object.name +" : "+ str(uni_object.mass) +","+ str(uni_object.radius) +" : "+ str(uni_object.x) +","+ str(uni_object.y) +","+ str(uni_object.z) +" : "+ str(uni_object.speed_x) +","+ str(uni_object.speed_y) +","+ str(uni_object.speed_z)
            
            if len(uni_object.force_vector_list) > 0:
                print "\tForce amount : angle2d : angle3d : start : stop"
                
                for force in uni_object.force_vector_list:
                    ( r, angle2d, angle3d ) = self.controller.universe.maths.xyz_to_angle(force.x, force.y, force.z)
                    print "\t"+str(r)+" : "+str(angle2d)+" : "+str(angle3d)+" : "+str(force.start)+" : "+str(force.stop)
            
    def x_play(self):
        self.list_uni_objects()
        obj_num = int(raw_input('Object number?\n'))
        time = float(raw_input('Step size in seconds?\n'))
        
        print "Calculating..."
        status, message = self.controller.animate(obj_num, time)
        
        print message
                
    def cli_save(self, command):
        file_name = self.get_attribute(command)
        if file_name is not None:
            self.controller.file_name = file_name
        status, message = self.controller.save()

        if status is not False:
            print "Simulation saved in " + self.controller.file_name

        print message
        
    def cli_load(self, command):
        file_name = self.get_attribute(command)
        if file_name is not None:
            self.controller.file_name = file_name
        status, message = self.controller.load()
        
        if status is not False:
            print "Simulation loaded from " + self.controller.file_name

        print message
        
    def get_attribute(self, command):
        clist = command.split(' ')
        if len(clist) > 1:
            return clist[1]
        return None
        
    def files(self):
        files = self.controller.list_files_in_folder()
        print files
        
    def set_copy_universe(self):
        status, message = self.controller.set_startpoint()
        print message
        
    def reverse_universe(self):
        status, message = self.controller.reverse_startpoint()
        print message
        
        
