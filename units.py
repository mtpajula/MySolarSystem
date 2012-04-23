

class Unit(object):
    '''
    Unit actions for set unit type
    '''
    
    def __init__(self, unit_dict, unit):
        
        self.unit = unit
        self.unit_dict = unit_dict
        
    def to_unit(self, number, given_unit):
        '''
        Returns Si value in given unit form
        
        @type  number:     int/float
        @param number:     Value in Si
        @type  given_unit: String
        @param given_unit: Given unit
        @return:           float value in given unit
        '''
        return number / self.unit_dict[given_unit]
        
    def to_unit_str(self, number, given_unit):
        '''
        Returns Si value in given unit form as string with unit name
        
        @type  number:     int/float
        @param number:     Value in Si
        @type  given_unit: String
        @param given_unit: Given unit
        @return:           string value in given unit and with unit name
        '''
        return str(self.to_unit(number, given_unit)) +' '+ given_unit
        
    def str(self, number):
        '''
        Returns Si value in default unit form as string with unit name
        
        @type  number:     int/float
        @param number:     Value in Si
        @return:           string value in default unit and with unit name
        '''
        return str(self.num(number)) +' '+ self.unit
        
    def num(self, number):
        '''
        Returns Si value in default unit form
        
        @type  number:     int/float
        @param number:     Value in Si
        @return:           float value in default unit
        '''
        if number is None:
            return None
        divider = self.unit_dict[self.unit]
        return float(number) / divider
        
    def set_unit(self, given_unit):
        '''
        Sets default unit to given unit
        '''
        for unit, divider in self.unit_dict.items():
            if unit == given_unit:
                self.unit = given_unit

    def si(self, number):
        '''
        Returns value in default unit as Si value
        
        @type  number:     int/float
        @param number:     Value in default unit
        @return:           float value in Si
        '''
        divider = self.unit_dict[self.unit]
        return float(number) * divider
        
    def to_si_from(self, number, given_unit):
        '''
        Returns value in given unit as Si value
        
        @type  number:     int/float
        @param number:     Value in given unit
        @type  given_unit: String
        @param given_unit: Given unit
        @return:           float value in Si
        '''
        return float(number) * self.unit_dict[given_unit]
        

class Units(object):
    '''
    Unit holder.
    Inits time, distance, mass, speed and force -units
    '''
    
    def __init__(self):
        
        self.default_time_unit = 's'
        self.default_dist_unit = 'm'
        self.default_mass_unit = 'kg'
        self.default_speed_unit = 'ms'
        self.default_force_unit = 'N'
        
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
        
        self.speed_units = {}
        self.speed_units['ms'] = 1
        self.speed_units['kmh'] = 1/3.6
        self.speed_units['kms'] = 1000
        
        self.force_units = {}
        self.force_units['N'] = 1
        self.force_units['dyne'] = 100000
        
        self.time = Unit(self.time_units, self.default_time_unit)
        self.dist = Unit(self.dist_units, self.default_dist_unit)
        self.mass = Unit(self.mass_units, self.default_mass_unit)
        self.speed = Unit(self.speed_units, self.default_speed_unit)
        self.force = Unit(self.force_units, self.default_force_unit)
        
    def save_units(self):
        '''
        Gives default units for saving in file
        
        @return: Dictionary
        '''
        units = {}
        units['time'] = self.time.unit
        units['dist'] = self.dist.unit
        units['mass'] = self.mass.unit
        units['speed'] = self.speed.unit
        units['force'] = self.force.unit
        
        return units
        
    def load_units(self, units):
        '''
        Sets default units from dictionary loaded from file
        
        @type  units: Dictionary
        @param units: Default units
        '''
        
        if 'time' in units:
            self.time.unit = units['time']
        if 'dist' in units:
            self.dist.unit = units['dist']
        if 'mass' in units:
            self.mass.unit = units['mass']
        if 'speed' in units:
            self.speed.unit = units['speed']
        if 'force' in units:
            self.force.unit = units['force']
