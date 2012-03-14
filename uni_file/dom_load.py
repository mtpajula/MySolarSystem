from xml.dom.minidom import parse
from universe.universe import Universe
from universe.uni_object import Uni_Object
from universe.force_vector import Force_Vector

class Dom_Load(object):
    
    def __init__(self):
        
        self.uni_list = []

    def load_simulation(self, file_name):
        
        print "load: " + file_name
        
        doc = parse(file_name)
        
        
        unis = doc.getElementsByTagName("universe")
        
        for uni in unis:
            self.uni_list.append(self.get_universe(uni))
        
        return self.uni_list

    def get_universe(self, uni):
        
        universe = Universe()
        
        step = uni.getAttribute("step")
        maths_time = uni.getElementsByTagName("maths")[0].getAttribute("time")
        
        step = int(step)
        maths_time = int(maths_time)
        universe.step = step
        universe.maths.time = maths_time
        
        objects = uni.getElementsByTagName("object")
        
        for obj in objects:
            universe.add_object(self.get_object(obj))
        
        return universe

    def get_object(self, obj):
        
        name = obj.getAttribute("name")
        massNode = obj.getElementsByTagName("mass")[0]
        mass = massNode.firstChild.nodeValue.strip()
        radiusNode = obj.getElementsByTagName("radius")[0]
        radius = radiusNode.firstChild.nodeValue.strip()
        
        uni_object = Uni_Object(name, mass, radius)
        
        coord = obj.getElementsByTagName("coordinates")[0]
        speed = obj.getElementsByTagName("speed_vector")[0]
        
        (x,y,z) = self.clean_xyz(coord)
        uni_object.x = x
        uni_object.y = y
        uni_object.z = z
        
        (x,y,z) = self.clean_xyz(speed)
        uni_object.speed_x = x
        uni_object.speed_y = y
        uni_object.speed_z = z

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
        
        forces = obj.getElementsByTagName("custom_force")
        
        for f in forces:
            uni_object.add_force_vector(self.get_force(f))
        
        return uni_object

    def get_force(self, f):
        
        vector = f.getElementsByTagName("vector")[0]
        
        (x,y,z) = self.clean_xyz(vector)
        
        force = Force_Vector(x, y, z)
        
        time = f.getElementsByTagName("time")[0]
        start = time.getAttribute("start")
        stop = time.getAttribute("stop")
        
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
        
        x = element.getAttribute("x")
        y = element.getAttribute("y")
        z = element.getAttribute("z")
        
        x = float(x)
        y = float(y)
        z = float(z)
        
        return (x,y,z)
        
