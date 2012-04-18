from xml.dom.minidom import parse
from universe.universe import Universe
from universe.uni_object import Uni_Object
from universe.force_vector import Force_Vector
from file_error import FileError

class Dom_Load(object):
    '''
    Loads simulation from file
    '''
    
    def __init__(self):
        
        self.uni_list = []
        self.pref_dict = {}

    def load_simulation(self, file_name):
        '''
        Loads simulation from given file
        '''
        
        print "load: " + file_name
        
        try:
            # Does xml parse to DOM
            doc = parse(file_name)
            unis = doc.getElementsByTagName("universe")
            
            if len(doc.getElementsByTagName("preferences")) > 0:
                pre = doc.getElementsByTagName("preferences")[0]
                self.get_preferences(pre)
            
            # Get universe-objects
            for uni in unis:
                self.uni_list.append(self.get_universe(uni))
            
            return (self.uni_list, self.pref_dict)
            
        except IOError:
            return None 
        
    def get_preferences(self, pre):
        '''
        read preferences dictionary
        '''
        
        for child in pre.childNodes: 
            
            if child.nodeType == 1:
                
                child_dict = {}
                
                if child.hasAttributes:
                    
                    for i in range(child.attributes.length):
                        a = child.attributes.item(i)
                        
                        child_dict[a.name] = a.value
                        
                self.pref_dict[child.nodeName] = child_dict

        
    def get_universe(self, uni):
        '''
        Loads universe-object from DOM
        '''
        universe = Universe()
        
        # Step and time
        step = uni.getAttribute("step")
        calc_time = uni.getAttribute("calc_time")
        maths_time = uni.getElementsByTagName("maths")[0].getAttribute("time")
        
        if calc_time == '':
            calc_time = '0'
        
        step = int(step)
        calc_time = int(calc_time)
        maths_time = int(maths_time)
        universe.step = step
        universe.calc_time = calc_time
        universe.maths.time = maths_time
        
        objects = uni.getElementsByTagName("object")
        
        for obj in objects:
            universe.add_object(self.get_object(obj))
        
        return universe

    def get_object(self, obj):
        '''
        Loads uni-object from DOM
        '''
        
        # name, mass, radius
        name = obj.getAttribute("name")
        massNode = obj.getElementsByTagName("mass")[0]
        mass = massNode.firstChild.nodeValue.strip()
        radiusNode = obj.getElementsByTagName("radius")[0]
        radius = radiusNode.firstChild.nodeValue.strip()
        
        uni_object = Uni_Object(name, mass, radius)
        
        # Location and speed vector
        coord = obj.getElementsByTagName("coordinates")[0]
        speed = obj.getElementsByTagName("speed_vector")[0]
        
        # Clean coordinates
        (x,y,z) = self.clean_xyz(coord)
        uni_object.x = x
        uni_object.y = y
        uni_object.z = z
        
        # Clean speed vector
        (x,y,z) = self.clean_xyz(speed)
        uni_object.speed_x = x
        uni_object.speed_y = y
        uni_object.speed_z = z

        # Object styles: type color
        styleNode = obj.getElementsByTagName("style")[0]
        object_type = styleNode.getAttribute("type")
        object_type = int(object_type)
        colorNode = styleNode.getElementsByTagName("color")[0]
        r = colorNode.getAttribute("r")
        b = colorNode.getAttribute("b")
        g = colorNode.getAttribute("g")
        r = int(r)
        b = int(b)
        g = int(g)
        
        uni_object.object_type = object_type
        uni_object.color = (r,b,g)
        
        # Force vectors
        forces = obj.getElementsByTagName("custom_force")
        
        for f in forces:
            uni_object.add_force_vector(self.get_force(f))
        
        return uni_object

    def get_force(self, f):
        '''
        Loads force-vectors from DOM
        '''
        vector = f.getElementsByTagName("vector")[0]
        
        # Clean force vector
        (x,y,z) = self.clean_xyz(vector)
        
        force = Force_Vector(x, y, z)
        
        # Start and stop times
        time = f.getElementsByTagName("time")[0]
        start = time.getAttribute("start")
        stop = time.getAttribute("stop")
        
        # None values
        if start != "None":
            start = int(start)
        else:
            start = None
        if stop != "None":
            stop = int(stop)
        else:
            stop = None
        
        force.start = start
        force.stop = stop
        
        return force
        
    def clean_xyz(self, element):
        '''
        Get float xyz values from coordinates element
        '''
        x = element.getAttribute("x")
        y = element.getAttribute("y")
        z = element.getAttribute("z")
        
        x = float(x)
        y = float(y)
        z = float(z)
        
        return (x,y,z)
        
