import xml.dom.minidom as dom
import sys, re

class Dom_Save(object):
    '''
    Saves given universies in file
    '''
    
    def __init__(self, pref_dict):
        
        self.uni_list = []
        self.pref_dict = pref_dict

    def add_universe(self, universe):
        '''
        Sets given universe to saving-list
        '''
        self.uni_list.append(universe)

    def save_simulation(self, file_name):
        '''
        Saves simulation in xml-file
        '''
        
        # Generate DOM representing simulation
        doc = self.generate_document()
        
        # Pretty xml :)
        docString = doc.toprettyxml("\t", "\n", "utf-8")
        
        # Write file
        try:
            f = open(file_name, "w")
            f.write(docString)
            f.close()
            
            return True, "Ok"
        except IOError:
            return False, "Failed to write file"
        
    
    def generate_document(self):
        '''
        Generates DOM representing simulation
        '''
        
        # root
        doc = dom.Document()
        root = doc.createElement("simulation")
        doc.appendChild(root)
        
        # Create preferences
        root.appendChild(self.generate_preferences(doc))
        
        # Loop given universes
        for i, universe in enumerate(self.uni_list):
            root.appendChild(self.generate_universe(doc, universe, i))
        
        return doc
        
    def generate_preferences(self, doc):
        
        pre = doc.createElement("preferences")
        
        for name, dictionary in self.pref_dict.items():
            
            element = doc.createElement(name)
            
            for attrname, item in dictionary.items():
                element.setAttribute(attrname, str(item))
                
            pre.appendChild(element)
            
        return pre
        
    def generate_universe(self, doc, universe, i):
        '''
        Returns universe in DOM
        '''
        
        # universe
        uni = doc.createElement("universe")
        uni.setAttribute("step", str(universe.step))
        uni.setAttribute("calc_time", str(universe.calc_time))
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
        '''
        Returns Object in DOM
        '''
        
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
        '''
        Returns forces in DOM
        '''
        
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
