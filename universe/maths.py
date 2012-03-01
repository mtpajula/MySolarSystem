import math

class Maths(object):
    
    def __init__(self):
        
        # Gravity constant
        self.f = 6.67 * 10**-11 # Nm^2/kg^2
        
        self.time = 1
        self.timejump = 3600*2 #3600*24
    
    def gravity(self, uni_obj1, uni_obj2):
        
        x = uni_obj2.x - uni_obj1.x
        y = uni_obj2.y - uni_obj1.y
        z = uni_obj2.z - uni_obj1.z

        r = math.sqrt(x**2 + y**2 + z**2)

        collision_dist = uni_obj1.radius + uni_obj2.radius

        if r > collision_dist:
            #print "distange: " + str(r)
            
            gforce = self.f * ( ( uni_obj1.mass * uni_obj2.mass ) / r**2 )
            
            #print "gforce: " + str(gforce)
            
            speed1 = ( gforce * self.time ) / uni_obj1.mass
            speed2 = ( gforce * self.time ) / uni_obj2.mass
            
            speed1 = speed1 * self.timejump
            speed2 = speed2 * self.timejump
            #print uni_obj1.name + " speed: " + str(speed1)
            #print uni_obj2.name + " speed: " + str(speed2)
            
            if x != 0:
                angle2d_obj1 = math.degrees( math.atan2( y,x ) )
            else:
                angle2d_obj1 = 90
            
            angle3d_obj1 = math.degrees( math.asin( z/r ) )

            if angle2d_obj1 > 0:
                angle2d_obj2 = angle2d_obj1 - 180
            else:
                angle2d_obj2 = 180 - math.fabs( angle2d_obj1 )
            
            angle3d_obj2 = angle3d_obj1 * -1

            
            #print "angle2d " + uni_obj1.name + ": " + str(angle2d_obj1)# + " = atan(" + str(y) + "/" + str(x) + ")"
            #print "angle3d " + uni_obj1.name + ": " + str(angle3d_obj1)# + " = asin(" + str(z) + "/" + str(r) + ")"
            
            #print "angle2d " + uni_obj2.name + ": " + str(angle2d_obj2)# + " = atan(" + str(y) + "/" + str(x) + ")"
            #print "angle3d " + uni_obj2.name + ": " + str(angle3d_obj2)# + " = asin(" + str(z) + "/" + str(r) + ")"
            
            self.add_vector(uni_obj1, speed1, angle2d_obj1, angle3d_obj1)
            self.add_vector(uni_obj2, speed2, angle2d_obj2, angle3d_obj2)
            
        else:
            
            print "collision"
            
            #self.add_vector(uni_obj1, uni_obj2.speed, uni_obj2.angle2d, uni_obj2.angle3d)
            
            self.collision(uni_obj1, uni_obj2)
            return uni_obj2

            
    def collision(self, uni_obj1, uni_obj2):
        
        ( x1, y1, z1 ) = self.get_vector_xyz(uni_obj1.speed, uni_obj1.angle2d, uni_obj1.angle3d)
        ( x2, y2, z2 ) = self.get_vector_xyz(uni_obj2.speed, uni_obj2.angle2d, uni_obj2.angle3d)
        
        m1 = uni_obj1.mass
        m2 = uni_obj2.mass
        
        print uni_obj1.name + " speed: " + str(uni_obj1.speed)
        print "angle2d " + uni_obj1.name + ": " + str(uni_obj1.angle2d)
        print "angle3d " + uni_obj1.name + ": " + str(uni_obj1.angle3d)
        
        print uni_obj2.name + " speed: " + str(uni_obj2.speed)
        print "angle2d " + uni_obj2.name + ": " + str(uni_obj2.angle2d)
        print "angle3d " + uni_obj2.name + ": " + str(uni_obj2.angle3d)
        
        print " x1: " + str(x1) + " y1: " + str(y1) + " z1: " + str(z1)
        print " x2: " + str(x2) + " y2: " + str(y2) + " z2: " + str(z2)
        
        x = self.collision_speed(x1, x2, m1, m2)
        y = self.collision_speed(y1, y2, m1, m2)
        z = self.collision_speed(z1, z2, m1, m2)
        
        print " x: " + str(x) + " y: " + str(y) + " z: " + str(z)
        
        uni_obj1.mass = m1 + m2
        
        print uni_obj1.mass
        
        ( speed, angle2d, angle3d ) = self.xyz_to_angle(x, y, z)
        uni_obj1.set_speed(speed, angle2d, angle3d)

        
        
    def collision_speed(self, v1, v2, m1, m2):
        
        u = (m1*v1 + m2*v2) / (m1 + m2)
        
        return u
        
    def move(self, uni_object):
        
        speed = uni_object.speed * self.timejump
        
        ( x, y, z ) = self.get_vector_xyz(speed, uni_object.angle2d, uni_object.angle3d)
        
        #print uni_object.name + " Added: x: " + str(x) + " y: " + str(y) + " z: " + str(z)
        
        uni_object.x += x
        uni_object.y += y
        uni_object.z += z
        
        #print uni_object.name + " new location: x: " + str(uni_object.x) + " y: " + str(uni_object.y) + " z: " + str(uni_object.z)
        
    def get_vector_xyz(self, speed, angle2d, angle3d):
        
        angle2d = math.radians( angle2d )
        angle3d = math.radians( angle3d )
        
        z = speed * math.sin( angle3d )
        c = speed * math.cos( angle3d )
        x = c * math.cos( angle2d )
        y = c * math.sin( angle2d )
        
        return ( x ,y ,z )
        
    def xyz_to_angle(self, x, y, z):
        if x != 0:
            angle2d = math.degrees( math.atan2( y,x ) )
        else:
            angle2d = 90
        
        r = math.sqrt(x**2 + y**2 + z**2)
        angle3d = math.degrees( math.asin( z/r ) )
        
        return ( r, angle2d, angle3d )
    
    def add_vector(self, uni_object, speed, angle2d, angle3d):
        
        ( x, y, z ) = self.get_vector_xyz(speed, angle2d, angle3d)
        ( x_old, y_old, z_old ) = self.get_vector_xyz(uni_object.speed, uni_object.angle2d, uni_object.angle3d)
        
        x += x_old
        y += y_old
        z += z_old
        
        #print uni_object.name + " Added vector: x: " + str(x) + " y: " + str(y) + " z: " + str(z)
        
        ( speed, angle2d, angle3d ) = self.xyz_to_angle(x, y, z)
        uni_object.set_speed(speed, angle2d, angle3d)
        
        
        
