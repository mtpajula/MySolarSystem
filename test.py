import unittest
from PySide import QtCore, QtGui
from controller import controller
from universe.maths import Maths
from cli.cli_pygame import Cli_Pygame
from universe.uni_object import Uni_Object
from universe.uni_object import Uni_Object
from gui.paint import Helper
import math
import os

class Test(unittest.TestCase):
    '''
    
    @author: Mikko Pajula
    
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
        
    def test_move_2(self):
        '''
        Test: Moving with gravity
        '''
        self.controller.universe.maths.time = 100000
        
        obj1 = self.controller.create_object("test1",5000000,1)
        obj2 = self.controller.create_object("test2",5000000,1)
        obj1.set_location(-100,0,0)
        obj2.set_location(100,0,0)
        
        self.controller.animate_step()
        
        r = math.sqrt(200**2 + 0**2)
        f = 6.67 * 10**-11 # Nm^2/kg^2
        speed1 = f * ( ( 100000 * obj2.mass ) / r**2 )
        lenght = speed1 * 100000
        
        obj1_travel = 100 + obj1.x
        
        self.assertEqual(round(lenght,1) ,round(obj1_travel,1),  "wrong distance moved")
        self.assertEqual(round(obj1.x,1) ,(-1*round(obj2.x,1)), "Both should move equally long distance")
        
    def test_move_3(self):
        '''
        Test: Moving with custom force vector
        '''
        self.controller.universe.maths.time = 50
        obj = self.controller.create_object("test",10,1)
        
        self.controller.create_angle_force(obj,1,0,0)
        
        f = 1.0
        m = 10.0
        t = 50.0
        
        a = f / m
        v = a * t
        s = v * t
        
        self.controller.animate_step()
        self.assertEqual(s ,round(obj.x),  "Wrong x location")
        
    def test_line_direction(self):
        '''
        Test: Draw line (lenght x) to same direction as given line
        '''
        color = QtGui.QColor(64, 32, 64)
        helper = Helper(self.controller, color, color)
        
        (x,y) = helper.line_direction(500,-500,0)
        
        lenght = math.sqrt(x**2 + y**2)
        self.assertEqual(10 ,round(lenght),  "Wrong lenght")
        
    def test_save_load(self):
        '''
        test file save and load
        '''
        
        obj = self.controller.create_object("test",10,2)
        self.controller.create_angle_force(obj,1,0,0)
        
        self.controller.file_name = 'test_py.xml'
        
        self.controller.save()
        
        self.controller.new_controller()
        
        self.assertEqual(False ,self.controller.not_empty(),  "Should be empty universe")
        
        self.controller.file_name = 'test_py.xml'
        self.controller.load()
        filePath = self.controller.folder + self.controller.file_name
        os.remove(filePath)
        
        
        self.assertEqual(True ,self.controller.not_empty(),  "Should not be empty universe")
        
        loadObj = self.controller.universe.object_list[0]
        
        self.assertEqual('test' ,loadObj.name,  "wrong object paramenters")
        self.assertEqual(10 ,loadObj.mass,  "wrong object paramenters")
        self.assertEqual(2 ,loadObj.radius,  "wrong object paramenters")
        
        loadForce = loadObj.force_vector_list[0]
        
        self.assertEqual(1 ,loadForce.x,  "wrong force object paramenters")

if __name__ == "__main__":
    unittest.main()
    
