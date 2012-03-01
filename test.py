import unittest

from controller import controller
from universe.maths import Maths
from cli.cli_pygame import Cli_Pygame
import math

class Test(unittest.TestCase):
    '''
    
    @author: Mikko Pajula 64570K
    
    '''


    def setUp(self):
        '''
        Sets up the initial state for all the test cases.
        '''
        self.controller = controller()
        self.maths = Maths()
        
        
        #aurinko = self.controller.create_object("aurinko","20","10")
        #maa = controller.create_object("maa","10","5")
        #kuu = self.controller.create_object("kuu","10","5")
        #maa.set_location(400,200,0)
        #kuu.set_location(200,-200,0)
        #aurinko.set_speed(0.3,45,0)
        
        
        aurinko = self.controller.create_object("aurinko","0","696000000.0")
        maa = self.controller.create_object("maa","0","6371000.0")
        
        kerroin = 10**21
        
        aurinko.mass = 1989100000.0 * kerroin
        maa.mass = 5973.6 * kerroin

        maa.set_location(149600000000.0,0,0)

        maa.set_speed(29780.0,90,0)
        
        
    def test_collision_speed(self):
        '''
        Test: Get name
        '''
        v1 = 1.0
        v2 = -2.0
        m1 = 20.0
        m2 = 20.0
        
        
        print self.maths.collision_speed(v1, v2, m1, m2)
        
    def test_pygame_scale(self):

        game = Cli_Pygame(self.controller)
        print self.controller.universe.object_list[1].name
        
        (x,y) = game.scale(self.controller.universe.object_list[1])
        
        print " x: " + str(x)
        print " y: " + str(y)
        
    def test_speed(self):

        print "\nspeed test"
        
        maa = self.controller.universe.object_list[1]
        
        x = maa.x
        y = maa.y
        
        day = 3600*24
        
        matka = x * math.pi * 2
        print "matka: " + str(matka)
        
        kesto = matka / maa.speed
        print "kesto: " + str(kesto)
        print "kesto paivissa: " + str(kesto / day)
        
        
        
        print "x: " + str(x)
        print "y: " + str(y)
        
if __name__ == "__main__":
    unittest.main()
    
