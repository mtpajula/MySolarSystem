import unittest
from PySide import QtCore, QtGui
from controller import controller
from universe.maths import Maths
from cli.cli_pygame import Cli_Pygame
from universe.uni_object import Uni_Object
from universe.uni_object import Uni_Object
from gui.paint import Helper
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
        
        
    def test_collision_speed(self):
        '''
        Test: Collision speed
        '''

        v1 = 1.0
        v2 = -2.0
        m1 = 20.0
        m2 = 20.0
        
        
        new_speed = self.maths.collision_speed(v1, v2, m1, m2)
        
        self.assertEqual(-0.5 ,new_speed,  "Wrong speed after collision")
        
    def test_get_vector_lenght(self):
        '''
        Test: sqrt(x^2 + y^2 + z^2)
        '''
        
        result = self.maths.get_vector_lenght(2,2,1)
        
        self.assertEqual(3 ,round(result),  "Wrong vector lenght")
        
    def test_xyz_to_angle(self):
        '''
        Test: xyz to angle
        '''
        
        (r,angle2d,angle3d) = self.maths.xyz_to_angle(2,2,1)
        
        self.assertEqual(3 ,round(r),  "Wrong vector lenght")
        self.assertEqual(45 ,round(angle2d),  "Wrong angle")
        
        (r,angle2d,angle3d) = self.maths.xyz_to_angle(3,4,-5)
        
        self.assertEqual(-45 ,round(angle3d),  "Wrong angle")
        
    def test_get_vector_xyz(self):
        '''
        Test: angle to xyz
        '''
        
        (x,y,z) = self.maths.get_vector_xyz(3,45,45)
        
        self.assertEqual(1.5 ,round(x,2),  "Wrong vector lenght")
        self.assertEqual(1.5 ,round(y,2),  "Wrong vector lenght")
        
        (r,angle2d,angle3d) = self.maths.xyz_to_angle(3,4,-5)
        (x,y,z) = self.maths.get_vector_xyz(r,angle2d,angle3d)
        
        self.assertEqual(3 ,round(x),  "Wrong vector lenght")
        self.assertEqual(4 ,round(y),  "Wrong vector lenght")
        self.assertEqual(-5 ,round(z),  "Wrong vector lenght")
        
    def test_move_1(self):
        '''
        Test: Moving with constant speed
        '''
        self.controller.universe.maths.time = 500
        
        obj = self.controller.create_object("test",1,1)
        
        self.controller.set_object_angle_speed(obj,1,0,0)
        
        self.controller.animate_step()
        
        self.assertEqual(500 ,round(obj.x),  "Wrong x location")
        
    def test_line_direction(self):
        '''
        Test: Draw line (lenght x) to same direction as given line
        '''
        background_color = QtGui.QColor(64, 32, 64)
        helper = Helper(self.controller, background_color)
        
        (x,y) = helper.line_direction(20,5)
        
        lenght = math.sqrt(x**2 + y**2)
        self.assertEqual(10 ,round(lenght),  "Wrong lenght")

if __name__ == "__main__":
    unittest.main()
    
