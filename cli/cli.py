
class Cli_Main(object):
    
    def __init__(self, controller):
        
        self.controller = controller
        '''
        self.commands = {
                        "quit"
                        }
        '''
    def print_help(self):
        
        print "My Solar System Command list:"
        print " - quit"
        print " - play"
        print " - pygame"
        print " - new object"
        print " - list objects"
        print " - set"
        print " - reverse"
        print " - xplay"
        print " - save"
        print " - load"
        print " - help"
        
    def menu(self):
        
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
                self.controller.set_startpoint()
                
            elif command == "reverse":
                self.controller.reverse_startpoint()
                
            elif command == "help":
                self.print_help()
                
            elif command == "xplay":
                self.x_play()
                
            elif command.startswith("save"):
                self.cli_save(command)
                
            elif command.startswith("load"):
                self.cli_load(command)
                
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
        
        
    def new_uni_object(self):
        
        name = raw_input('name?\n')
        mass = raw_input('mass?\n')
        radius = raw_input('radius?\n')
        
        new_obj = self.controller.create_object(name, mass, radius)
        
        print "done"
        
    def list_uni_objects(self):
        
        print "step: " + str(self.controller.universe.step)
        print "Name : mass,radius : x,y,z : speed_x,speed_y,speed_z"
        
        for uni_object in self.controller.universe.get_object_list():
            print uni_object.name +" : "+ str(uni_object.mass) +","+ str(uni_object.radius) +" : "+ str(uni_object.x) +","+ str(uni_object.y) +","+ str(uni_object.z) +" : "+ str(uni_object.speed_x) +","+ str(uni_object.speed_y) +","+ str(uni_object.speed_z)
            
            if len(uni_object.force_vector_list) > 0:
                print "\tForce amount : angle2d : angle3d : start : stop"
                
                for force in uni_object.force_vector_list:
                    ( r, angle2d, angle3d ) = self.controller.universe.maths.xyz_to_angle(force.x, force.y, force.z)
                    print "\t"+str(r)+" : "+str(angle2d)+" : "+str(angle3d)+" : "+str(force.start)+" : "+str(force.stop)
            
    def x_play(self):
        
        running = True
        
        self.controller.save()
        
        while running:
            
            
            day = 24
            month = day*30
            year = day*365
            
            if (self.controller.universe.step % month) == 0:
                #print "month: " + str(self.controller.universe.step)
                x = self.controller.universe.object_list[1].x / self.controller.copy_universe.object_list[1].x
                x = str(x).replace(".",",")
                print x
            
            if self.controller.universe.step > year:
                running = False
            
            self.controller.animate_step()
                
    def cli_save(self, command):
        file_name = self.get_attribute(command)
        if file_name is not None:
            self.controller.file_name = file_name
        self.controller.save()
        
    def cli_load(self, command):
        file_name = self.get_attribute(command)
        if file_name is not None:
            self.controller.file_name = file_name
        self.controller.load()
        
    def get_attribute(self, command):
        clist = command.split(' ')
        if len(clist) > 1:
            return clist[1]
        return None
        
        
        
