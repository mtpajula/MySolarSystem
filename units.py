

class Unit(object):
    
    def __init__(self, unit_dict, unit):
        
        self.unit = unit
        self.unit_dict = unit_dict
        
    def to_unit(self, number, given_unit):
        return number / self.unit_dict[given_unit]
        
    def str(self, number):
        return str(self.num(number)) +' '+ self.unit
        
    def num(self, number):
        '''
        returns given SI num in  given unit
        '''
        divider = self.unit_dict[self.unit]
        return number / divider
        
    def set_unit(self, given_unit):
        
        for unit, divider in self.unit_dict.items():
            if unit == given_unit:
                self.unit = given_unit



class Units(object):
    
    def __init__(self):
        
        self.default_time_unit = 's'
        self.default_dist_unit = 'm'
        self.default_mass_unit = 'kg'
        
        self.time_units = {}
        self.time_units['s'] = 1
        self.time_units['h'] = 3600
        self.time_units['d'] = 3600*24
        self.time_units['m'] = 3600*24*30
        self.time_units['y'] = 3600*24*365
        
        self.dist_units = {}
        self.dist_units['m'] = 1
        self.dist_units['km'] = 1000
        self.dist_units['1000km'] = 1000*1000
        self.dist_units['100000km'] = 1000*100000
        self.dist_units['au'] = 149598000000
    
        self.mass_units = {}
        self.mass_units['kg'] = 1
        self.mass_units['t'] = 1000
        self.mass_units['kt'] = 1000*1000
        self.mass_units['mt'] = 1000*1000*1000
        self.mass_units['10-21kg'] = 1 * 10**21
        
        self.time = Unit(self.time_units, self.default_time_unit)
        self.dist = Unit(self.dist_units, self.default_dist_unit)
        self.mass = Unit(self.mass_units, self.default_mass_unit)
        
    def save_units(self):
        
        units = {}
        units['time_unit'] = self.time.unit
        units['dist_unit'] = self.dist.unit
        units['mass_unit'] = self.mass.unit
        
        return units
        
    def load_units(self, units):
        
        self.time.unit = units['time_unit']
        self.dist.unit = units['dist_unit']
        self.mass.unit = units['mass_unit']
