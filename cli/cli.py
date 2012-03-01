
class Cli_Main(object):
    
    def __init__(self, controller):
        
        self.controller = controller
        '''
        self.commands = {
                        "quit"
                        }
        '''
    
    def menu(self):
        
        quit_cli = False
        print "My Solar System Command list:"
        print " - quit"
        print " - play"
        print " - pygame"
        print " - new object"
        print " - list objects"
        
        print "\n"
        
        while quit_cli is False:
            
            
            
            command = raw_input('Command?\n')
            
            if command == "quit":
                print "bye!"
                quit_cli = True
            
            if command == "play":
                self.play()
                
            if command == "pygame":
                self.pygame()
                
            if command == "new object":
                self.new_uni_object()
                
            if command == "list objects":
                self.list_uni_objects()
                
            print "\n"
            
    
    def play(self):
        
        self.controller.universe.calculate_gravity()
        self.controller.universe.move_objects()
        #self.controller.animate()
        
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
        
        print "Name : mass,radius : x,y,z : speed,angle2d,angle3d"
        
        for uni_object in self.controller.universe.get_object_list():
            print uni_object.name +" : "+ str(uni_object.mass) +","+ str(uni_object.radius) +" : "+ str(uni_object.x) +","+ str(uni_object.y) +","+ str(uni_object.z) +" : "+ str(uni_object.speed) +","+ str(uni_object.angle2d) +","+ str(uni_object.angle3d)
        
        
        
        
