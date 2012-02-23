

class Universe(object):
    
    def __init__(self):
        
        self.object_list = []
    
    def add_object(self, uni_object):
        
        self.object_list.append(uni_object)

    def get_object_list(self):
        
        return self.object_list
