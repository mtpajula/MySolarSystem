import math

class Maths(object):
    
    def __init__(self):
        
        # Gravity constant
        self.f = 6.67 * 10**-11 # Nm^2/kg^2
        
        self.time = 3600
        self.timejump = 3600#*2 #3600*24
        
        self.rungekutta = False
    
    
    def set_step(self, step):
        '''
        FAIL
        '''
        self.time = step**2

    
    def gravity(self, uni_obj1, uni_obj2):
        
        x = uni_obj2.x - uni_obj1.x
        y = uni_obj2.y - uni_obj1.y
        z = uni_obj2.z - uni_obj1.z

        #r = math.sqrt(x**2 + y**2 + z**2)
        r = self.get_vector_lenght(x, y, z)

        collision_dist = uni_obj1.radius + uni_obj2.radius

        if r > collision_dist:
            #print "distange: " + str(r)
            
            gforce = self.f * ( ( uni_obj1.mass * uni_obj2.mass ) / r**2 )
            
            #print "gforce: " + str(gforce)
            
            speed1 = ( gforce * self.time ) / uni_obj1.mass
            speed2 = ( gforce * self.time ) / uni_obj2.mass
            
            #speed1 = speed1 * self.timejump
            #speed2 = speed2 * self.timejump
            #print uni_obj1.name + " speed: " + str(speed1)
            #print uni_obj2.name + " speed: " + str(speed2)
                
            scale1 = speed1 / r
            scale2 = speed2 / r
            
            x1 = scale1 * x
            y1 = scale1 * y
            z1 = scale1 * z
            
            x2 = scale2 * x * -1
            y2 = scale2 * y * -1
            z2 = scale2 * z * -1
            
            #print " x1: " + str(x1) + " y1: " + str(y1) + " z1: " + str(z1)
            #print " x2: " + str(x2) + " y2: " + str(y2) + " z2: " + str(z2)
            
            r1 = math.sqrt(x1**2 + y1**2 + z1**2)
            #print "r1: " + str(r1)
            
            r2 = math.sqrt(x2**2 + y2**2 + z2**2)
            #print "r2: " + str(r2)
            
            self.add_vector(uni_obj1, x1, y1, z1)
            self.add_vector(uni_obj2, x2, y2, z2)

        else:
            
            print "collision"

            self.collision(uni_obj1, uni_obj2)
            return uni_obj2

    def runge_kutta_4(self, t, v, vk):
        
        h = self.time
        
        f1 = h * self.formula(vk, t, v)
        f2 = h * self.formula(vk, ( t+h/2 ), ( v+f1/2 ))
        f3 = h * self.formula(vk, ( t+h/2 ), ( v+f2/2 ))
        f4 = h * self.formula(vk, t, ( v+f3 ))
        
        speed = v + (1/6)*(f1 + 2*f2 + 3*f3 + f4)
        
        return speed
        
    def formula(self, vk, t, v):
        
        v = v + vk
        return v
        
            
    def collision(self, uni_obj1, uni_obj2):
        
        x1 = uni_obj1.speed_x
        y1 = uni_obj1.speed_y
        z1 = uni_obj1.speed_z
        
        x2 = uni_obj2.speed_x
        y2 = uni_obj2.speed_y
        z2 = uni_obj2.speed_z
        
        m1 = uni_obj1.mass
        m2 = uni_obj2.mass
        
        print " x1: " + str(x1) + " y1: " + str(y1) + " z1: " + str(z1)
        print " x2: " + str(x2) + " y2: " + str(y2) + " z2: " + str(z2)
        
        x = self.collision_speed(x1, x2, m1, m2)
        y = self.collision_speed(y1, y2, m1, m2)
        z = self.collision_speed(z1, z2, m1, m2)
        
        print " x: " + str(x) + " y: " + str(y) + " z: " + str(z)
        
        uni_obj1.mass = m1 + m2
        
        print uni_obj1.mass
        
        uni_obj1.set_speed(x, y, z)
        
        
    def collision_speed(self, v1, v2, m1, m2):
        
        u = (m1*v1 + m2*v2) / (m1 + m2)
        
        return u
        
    def get_vector_lenght(self, x, y, z):
        return math.sqrt(x**2 + y**2 + z**2)
        
    def force_vector_effect(self, force, uni_object):

        f = self.get_vector_lenght(force.x, force.y, force.z)
        
        s = self.get_vector_lenght(uni_object.x, uni_object.y, uni_object.z)
        
        speed = ( f * self.time ) / uni_object.mass
        
        scale = speed / f
        
        x = scale * force.x
        y = scale * force.y
        z = scale * force.z
        
        #print " x: " + str(x) + " y: " + str(y) + " z: " + str(z)
        #print " f: " + str(f) + " s: " + str(s) + " speed: " + str(speed)
        
        self.add_vector(uni_object, x, y, z)
        
    def move(self, uni_object, step):
        
        # Force vector effect
        for force in uni_object.force_vector_list:
            
            if force.start is None:
                if force.stop is None:
                    self.force_vector_effect(force, uni_object)
                elif force.stop > step:
                    self.force_vector_effect(force, uni_object)   
            elif force.start <= step:
                if force.stop is None:
                    self.force_vector_effect(force, uni_object)
                elif force.stop > step:
                    self.force_vector_effect(force, uni_object)
        
        
        if self.rungekutta is True:
            uni_object.x = self.runge_kutta_4(step, uni_object.x, uni_object.speed_x)
            uni_object.y = self.runge_kutta_4(step, uni_object.y, uni_object.speed_y)
            uni_object.z = self.runge_kutta_4(step, uni_object.z, uni_object.speed_z)
        else:
            uni_object.x += uni_object.speed_x * self.time
            uni_object.y += uni_object.speed_y * self.time
            uni_object.z += uni_object.speed_z * self.time
        
        #print "move:"
        #print uni_object.name + " Added: x: " + str(uni_object.speed_x) + " y: " + str(uni_object.speed_y) + " z: " + str(uni_object.speed_z)
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
        
    def add_vector(self, uni_object, x, y, z):
        
        uni_object.speed_x += x
        uni_object.speed_y += y
        uni_object.speed_z += z
