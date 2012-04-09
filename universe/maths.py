import math

class Maths(object):
    '''
    Class, that does all the gravity and additional force vector calculations
    
    '''
    
    def __init__(self):
        
        # Gravity constant
        self.f = 6.67 * 10**-11 # Nm^2/kg^2
        
        # Time value used in calculations
        # Also defines accuracy
        self.time = 3600
        
        # If False: Euler
        # If True: Runge kutta (Not yet functional)
        self.rungekutta = False
    
    def gravity(self, uni_obj1, uni_obj2):
        '''
        Calculates gravity speed vectors for both given object
        '''
        
        x = uni_obj2.x - uni_obj1.x
        y = uni_obj2.y - uni_obj1.y
        z = uni_obj2.z - uni_obj1.z
        
        # Distange between objects
        r = self.get_vector_lenght(x, y, z)
        
        # Collision happens if radius1+radius2 < r
        collision_dist = uni_obj1.radius + uni_obj2.radius

        if r > collision_dist:
            
            # F = G*m1*m2/r^2
            gforce = self.f * ( ( uni_obj1.mass * uni_obj2.mass ) / r**2 )

            # v = F*t/m
            speed1 = ( gforce * self.time ) / uni_obj1.mass
            speed2 = ( gforce * self.time ) / uni_obj2.mass
            
            # Speed vector has identical form with the lenght-vector
            # Speed vector is therefore calculated using scale-value
            # Between each xyz
            scale1 = speed1 / r
            scale2 = speed2 / r
            
            x1 = scale1 * x
            y1 = scale1 * y
            z1 = scale1 * z
            
            x2 = scale2 * x * -1
            y2 = scale2 * y * -1
            z2 = scale2 * z * -1
            
            self.add_vector(uni_obj1, x1, y1, z1)
            self.add_vector(uni_obj2, x2, y2, z2)

        else:
            # Collision
            print "collision"

            self.collision(uni_obj1, uni_obj2)
            # object 2 is deleted
            return uni_obj2

    def runge_kutta_4(self, t, v, vk):
        '''
        TODO Runge-kutta
        '''
        h = self.time
        
        f1 = h * self.formula(vk, t, v)
        f2 = h * self.formula(vk, ( t+h/2 ), ( v+f1/2 ))
        f3 = h * self.formula(vk, ( t+h/2 ), ( v+f2/2 ))
        f4 = h * self.formula(vk, t, ( v+f3 ))
        
        speed = v + (1/6)*(f1 + 2*f2 + 3*f3 + f4)
        
        return speed
        
    def formula(self, vk, t, v):
        '''
        TODO: Runge-kutta
        '''
        v = v + vk
        return v
        
            
    def collision(self, uni_obj1, uni_obj2):
        '''
        In collision between two given objects
        object1 gets momentum and other object's mass
        '''
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
        '''
        Speed after collision
        '''
        u = (m1*v1 + m2*v2) / (m1 + m2)
        
        return u
        
    def get_vector_lenght(self, x, y, z):
        '''
        Returns given 3d vectors lenght
        '''
        return math.sqrt(x**2 + y**2 + z**2)
        
    def force_vector_effect(self, force, uni_object):
        '''
        Calculates new speed vector for object using given
        Force vector 
        '''

        f = self.get_vector_lenght(force.x, force.y, force.z)
        s = self.get_vector_lenght(uni_object.x, uni_object.y, uni_object.z)
        
        speed = ( f * self.time ) / uni_object.mass
        
        scale = speed / f
        
        x = scale * force.x
        y = scale * force.y
        z = scale * force.z
        
        self.add_vector(uni_object, x, y, z)
        
    def move(self, uni_object, step):
        '''
        Moves given object based on it's speed vector
        and it's enabled force vectors
        '''
        
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
        
        # Rungekutta or not
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
        '''
        Transforms angle-vector to xyz-vector
        '''
        angle2d = math.radians( angle2d )
        angle3d = math.radians( angle3d )
        
        z = speed * math.sin( angle3d )
        c = speed * math.cos( angle3d )
        x = c * math.cos( angle2d )
        y = c * math.sin( angle2d )
        
        return ( x ,y ,z )
        
    def xyz_to_angle(self, x, y, z):
        '''
        Transforms xyz-vector to angle-vector
        '''
        if x != 0:
            angle2d = math.degrees( math.atan2( y,x ) )
        else:
            angle2d = 90
        
        r = self.get_vector_lenght(x,y,z)
        
        angle3d = math.degrees( math.asin( z/r ) )
        
        return ( r, angle2d, angle3d )
        
    def add_vector(self, uni_object, x, y, z):
        '''
        Sums new given vector to current one
        '''
        uni_object.speed_x += x
        uni_object.speed_y += y
        uni_object.speed_z += z
