from PySide import QtCore, QtGui
import math


class Helper:
    def __init__(self, controller, background_color):
        
        self.width = 200
        self.height = 200
        
        self.controller = controller
        
        self.largest_mass_object = None
        
        self.scale_factor = 1
        self.center_x = 0
        self.center_y = 0
        
        if self.controller.not_empty():
            self.get_scale_factor()
        
        self.set_background_color(background_color)
        
        self.textPen = QtGui.QPen(QtCore.Qt.white)
        self.textFont = QtGui.QFont()
        self.textFont.setPixelSize(20)
        
    def set_background_color(self, color):
        
        self.background_color = color
        self.background = QtGui.QBrush(self.background_color)
        
    def save_background_color(self):
        
        dictionary = {}
        dictionary['r'] = self.background_color.red()
        dictionary['g'] = self.background_color.green()
        dictionary['b'] = self.background_color.blue()
        
        return dictionary
        
    def load_background_color(self, dictionary):
        
        background_color = QtGui.QColor(int(dictionary['r']), int(dictionary['g']), int(dictionary['b']))
        self.set_background_color(background_color)
        
    def get_largest_mass_object(self):
        '''
        Finds largest mass object in universe
        '''
        largest_mass_object = None
        largest_mass = 0
        
        for uni_object in self.controller.universe.object_list:
            if uni_object.mass > largest_mass:
                largest_mass = uni_object.mass
                largest_mass_object = uni_object

        self.largest_mass_object = largest_mass_object
        self.center_x = largest_mass_object.x
        self.center_y = largest_mass_object.y
        
    def get_max_dist(self, max_dist):
        '''
        Finds max xy distange between universe objects
        '''
        object_list = self.controller.universe.object_list
            
        amount = len(object_list)
        
        for i in range(amount):
            
            j = i + 1
            
            for k in range(j, amount):
                
                x = math.fabs(object_list[i].x - object_list[k].x)
                y = math.fabs(object_list[i].y - object_list[k].y)
                
                if x > max_dist:
                    max_dist = x
                    
                if y > max_dist:
                    max_dist = y
        
        return max_dist
        
    def get_scale_factor(self):
        '''
        Calculates scale factor using max distange in universe
        
        Max distange is scaled, that screen min / 2 represents max dist  
        '''
        if self.controller.not_empty():
            
            
            
            self.get_largest_mass_object()
            init_max = self.largest_mass_object.radius * 100
            
            max_dist = self.get_max_dist(init_max)
            
            screen_min = self.width
            
            if self.width > self.height:
                screen_min = self.height
                
            screen_min = screen_min / 2.0
            
            scale_factor = screen_min / max_dist
            
            self.scale_factor = scale_factor
        
    def scale(self, uni_object):
        '''
        Scales object locations for pygame window
        '''
        
        x =  uni_object.x - self.center_x
        y =  uni_object.y - self.center_y
        
        x = self.scale_factor * x
        y = self.scale_factor * y
        
        x = int(  + x )
        y = int(  - y )
        
        return ( x, y )

    def paint(self, painter, event):
        
        painter.fillRect(event.rect(), self.background)
        painter.translate(painter.device().width()/2, painter.device().height()/2)

        painter.save()
        
        for uni_object in self.controller.universe.object_list:

            ( x, y ) = self.scale(uni_object)
            
            (r,g,b) = uni_object.color
            color = QtGui.QColor(r, g, b)
            
            painter.setBrush(color)
            painter.setPen(color)
            
            size = uni_object.object_type * 2
            fix = size/2
            
            painter.drawEllipse(x-fix, y-fix, size, size)
            
        painter.restore()
        
        painter.setPen(self.textPen)
        painter.setFont(self.textFont)
        time = self.controller.units.time.num(self.controller.universe.calc_time)
        text = str(round(time, 1)) + ' ' +  self.controller.units.time.unit
        painter.drawText(QtCore.QRect(self.width/2-100, self.height/2-100, 100, 100), 
                            QtCore.Qt.AlignCenter, text)
            

class Widget(QtGui.QWidget):
    def __init__(self, helper, parent = None):
        QtGui.QWidget.__init__(self)
        
        self.helper = helper
        self.animating = False

    def animate(self):
        self.animating = True
        
        for i in range(self.helper.controller.steps_between_paint):
            self.helper.controller.animate_step()
        
        self.repaint()
        self.animating = False

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        if self.animating is False:
            self.helper.width = painter.device().width()
            self.helper.height = painter.device().height()
            self.helper.get_scale_factor()
        
        self.helper.paint(painter, event)
        painter.end()
