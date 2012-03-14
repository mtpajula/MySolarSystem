import xml.dom.minidom as dom
import sys, re

class Dom_Save(object):
    
    def __init__(self):
        
        self.uni_list = []

    def add_universe(self, universe):
        
        self.uni_list.append(universe)

    def save_simulation(self, file_name):
        
        doc = self.generate_document()
        
        docString = doc.toprettyxml("\t", "\n", "utf-8")
        #sprint docString
        
        f = open(file_name, "w")
        f.write(docString)
        f.close()
        
    
    def generate_document(self):
        
        # root
        doc = dom.Document()
        root = doc.createElement("simulation")
        doc.appendChild(root)
        
        for i, universe in enumerate(self.uni_list):
            root.appendChild(self.generate_universe(doc, universe, i))
        
        return doc
        
    def generate_universe(self, doc, universe, i):
        
        # universe
        uni = doc.createElement("universe")
        uni.setAttribute("step", str(universe.step))
        id_str = "00" + str(i+1)
        uni.setAttribute("id", str(id_str))

        # maths time
        maths = doc.createElement("maths")
        maths.setAttribute("time", str(universe.maths.time))
        uni.appendChild(maths)
        
        for uni_object in universe.object_list:
            uni.appendChild(self.generate_object(doc, uni_object))
        
        return uni

    def generate_object(self, doc, uni_object):
        
        obj = doc.createElement("object")
        
        # name
        obj.setAttribute("name", str(uni_object.name))
        
        # mass
        mass = doc.createElement("mass")
        txt = doc.createTextNode(str(uni_object.mass))
        mass.appendChild(txt)
        obj.appendChild(mass)
        
        # radius
        radius = doc.createElement("radius")
        txt = doc.createTextNode(str(uni_object.radius))
        radius.appendChild(txt)
        obj.appendChild(radius)
        
        # coordinates
        coordinates = doc.createElement("coordinates")
        coordinates.setAttribute("x", str(uni_object.x))
        coordinates.setAttribute("y", str(uni_object.y))
        coordinates.setAttribute("z", str(uni_object.z))
        obj.appendChild(coordinates)
        
        # speed vector
        coordinates = doc.createElement("speed_vector")
        coordinates.setAttribute("x", str(uni_object.speed_x))
        coordinates.setAttribute("y", str(uni_object.speed_y))
        coordinates.setAttribute("z", str(uni_object.speed_z))
        obj.appendChild(coordinates)
        
        # style
        style = doc.createElement("style")
        style.setAttribute("type", str(uni_object.object_type))
        # color
        color = doc.createElement("color")
        (r,b,g) = uni_object.color
        color.setAttribute("r", str(r))
        color.setAttribute("b", str(b))
        color.setAttribute("g", str(g))
        
        style.appendChild(color)
        obj.appendChild(style)
        
        # force vectors
        if len(uni_object.force_vector_list) > 0:
            forces = doc.createElement("custom_forces")
            for force in uni_object.force_vector_list:
                forces.appendChild(self.generate_force(doc, force))
            obj.appendChild(forces)
        
        return obj
        
    def generate_force(self, doc, force):
        
        f = doc.createElement("custom_force")
        
        # coordinates
        vector = doc.createElement("vector")
        vector.setAttribute("x", str(force.x))
        vector.setAttribute("y", str(force.y))
        vector.setAttribute("z", str(force.z))
        f.appendChild(vector)
        
        # coordinates
        time = doc.createElement("time")
        time.setAttribute("start", str(force.start))
        time.setAttribute("stop", str(force.stop))
        f.appendChild(time)
        
        return f
