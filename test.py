import unittest

from controller import controller
from universe.maths import Maths
from cli.cli_pygame import Cli_Pygame
from universe.uni_object import Uni_Object
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
        
        self.distange = 149600000000.0
        
        maa.set_location(self.distange,0,0)

        maa.set_speed(29780.0,90,0)
        
        self.controller.universe.transfer_speed_angles_to_xyz()
        
        self.controller.save()
        
        
    def test_collision_speed(self):
        '''
        Test: Get name
        '''
        
        print "\ncollision speed test"
        
        v1 = 1.0
        v2 = -2.0
        m1 = 20.0
        m2 = 20.0
        
        
        print self.maths.collision_speed(v1, v2, m1, m2)
        
    def test_pygame_scale(self):

        game = Cli_Pygame(self.controller)
        print self.controller.universe.object_list[1].name
        
        (x,y) = game.scale(self.controller.universe.object_list[1])
        
        print "\npygame scale test"
        
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
        
    def test_runge_kutta(self):
        
        print "\nrunge kutta test"
        
        runge = Maths()
        runge.time = 1
        test = Uni_Object("test", "10", "5")
        test.xyz = True
        
        test.set_speed_xyz(10, 0, 0)
        step = 1
        
        runge.move(test, step)
        
        print test.name + " Added: x: " + str(test.speed_x) + " y: " + str(test.speed_y) + " z: " + str(test.speed_z)
        print test.name + " new location: x: " + str(test.x) + " y: " + str(test.y) + " z: " + str(test.z)
        
        test.set_location(0, 0, 0)
        test.set_speed_xyz(10, 0, 0)
        runge.rungekutta = True
        runge.move(test, step)
        
        print test.name + " Added: x: " + str(test.speed_x) + " y: " + str(test.speed_y) + " z: " + str(test.speed_z)
        print test.name + " new location: x: " + str(test.x) + " y: " + str(test.y) + " z: " + str(test.z)
        
        
    def test_accuracy(self):
        
        print "\nAccuracy test"
        
        c = controller()

        aurinko = c.create_object("aurinko","1150","1")
        maa = c.create_object("maa","100","1")
        follow = 1 # maa
        
        maa.set_location(30.0,0.0,0)
        maa.set_speed_xyz(0,0,0)

        c.save()
        
        xyz1 = c.animate(10000, 1, 1000, follow)
        #xyz1 = c.animate(100, 100, 10, follow)
        
        c.load()

        xyz2 = c.animate(5000, 2, 500, follow)
        
        c.load()
        
        xyz3 = c.animate(1000, 10, 100, follow)
        
        c.load()
        
        xyz4 = c.animate(100, 100, 10, follow)
        
        for i in range(10):
            x1 = str(xyz1[0][i]).replace(".",",")
            x2 = str(xyz2[0][i]).replace(".",",")
            x3 = str(xyz3[0][i]).replace(".",",")
            x4 = str(xyz4[0][i]).replace(".",",")
            
            
            
            print x1 +";"+ x2 +";"+ x3 +";"+ x4
            
    def test_accuracy_2(self):
        
        print "\nAccuracy test 2"

        follow = 1 # maa
        
        xyz1 = self.controller.animate(365, 3600, 30, follow)
        #xyz1 = c.animate(100, 100, 10, follow)
        
        #self.controller.load()

        #xyz2 = self.controller.animate(3650, 1, 37, follow)
        
        #self.controller.load()
        
        #xyz3 = self.controller.animate(1000, 10, 100, follow)
        
        #self.controller.load()
        
        #xyz4 = self.controller.animate(100, 100, 10, follow)

        for i in range(len(xyz1[0])):
            x1 = str(self.distange-xyz1[0][i]).replace(".",",")
            #x2 = str(xyz2[0][i]).replace(".",",")
            #x3 = str(xyz3[0][i]).replace(".",",")
            #x4 = str(xyz4[0][i]).replace(".",",")
            
            
            
            print x1# +";"+ x2 +";"+ x3 +";"+ x4
        
if __name__ == "__main__":
    unittest.main()
    
