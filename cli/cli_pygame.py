import math
import pygame
from pygame import *


class Cli_Pygame(object):
    
    def __init__(self, controller):
        
        self.controller = controller
        
        self.width = 1440
        self.height = 900
        
        self.largest_mass_object = self.get_largest_mass_object()
        
        self.center_x = self.largest_mass_object.x
        self.center_y = self.largest_mass_object.y

        self.scale_factor = self.get_scale_factor()
    
    def get_largest_mass_object(self):
        largest_mass_object = None
        largest_mass = 0
        
        for uni_object in self.controller.universe.object_list:
            if uni_object.mass > largest_mass:
                largest_mass = uni_object.mass
                largest_mass_object = uni_object

        return largest_mass_object
        
    def get_max_dist(self, max_dist):
        
        object_list = self.controller.universe.object_list
            
        amount = len(object_list)
        
        for i in range(amount):
            
            j = i + 1
            
            for k in range(j, amount):
                
                x = math.fabs(object_list[i].x - object_list[k].x)
                y = math.fabs(object_list[i].y - object_list[k].y)
                
                #print "x: " + str(x)
                #print "y: " + str(y)
                
                if x > max_dist:
                    max_dist = x
                    
                if y > max_dist:
                    max_dist = y
        
        return max_dist
        
    def get_scale_factor(self):
        
        init_max = self.largest_mass_object.radius * 100
        max_dist = self.get_max_dist(init_max)
        
        screen_min = self.width
        
        if self.width > self.height:
            screen_min = self.height
            
        screen_min = screen_min / 2.0
        
        print "screen_min: " + str(screen_min)
        print "max_dist: " + str(max_dist)
        
        scale_factor = screen_min / max_dist
        
        print "scale_factor: " + str(scale_factor)
        
        return scale_factor
        
    def scale(self, uni_object):
        
        #x = self.largest_mass_object.x - uni_object.x
        #y = self.largest_mass_object.y - uni_object.y
        x = uni_object.x - self.center_x
        y = uni_object.y - self.center_y
        
        x = self.scale_factor * x
        y = self.scale_factor * y
        
        x = self.width / 2 + x
        y = self.height / 2 - y
        
        #print uni_object.name + " x: " + str(x)
        #print uni_object.name + " y: " + str(y)
        
        return ( x, y )
        
    
    def start_animation(self):
        
        pygame.init()
        BG_colour = (0,0,0)
        #particle_colour = (255,255,255)
        screen = pygame.display.set_mode((self.width, self.height))

        running = True
        
        time = 1

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            screen.fill(BG_colour)
            
            self.controller.animate_step()
            time += 1
            #print "time (day): " + str(time)
            
            for uni_object in self.controller.universe.object_list:
                
                #x = self.width / 2 + uni_object.x
                #y = self.height / 2 - uni_object.y
                
                ( x, y ) = self.scale(uni_object)
                
                #pygame.draw.rect(screen, particle_colour, (int(x), int(y), uni_object.radius), uni_object.radius)
                pygame.draw.circle(screen, uni_object.color, (int(x), int(y)), uni_object.object_type, 0)
              
            pygame.display.flip()
        
        pygame.quit()
