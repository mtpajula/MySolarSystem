from PySide import QtCore, QtGui
import math


class Helper:
    '''
    Draws objects in QPaint
    Code originally from:
    U{http://qt.gitorious.org/pyside/pyside-examples/blobs/e853ca94f7ccd122d3498fe562db5d28c4e37edb/examples/opengl/2dpainting.py}
    '''
    
    def __init__(self, controller, background_color, line_color):
        
        self.width = 200
        self.height = 200
        
        self.line_lenght = 10
        self.draw_lines = True
        
        self.controller = controller
        
        self.largest_mass_object = None
        
        self.scale_factor = 1
        self.center_x = 0
        self.center_y = 0
        
        if self.controller.not_empty():
            self.get_scale_factor()
        
        self.set_background_color(background_color)
        self.set_line_color(line_color)
        
        self.textPen = QtGui.QPen(QtCore.Qt.white)
        self.textFont = QtGui.QFont()
        self.textFont.setPixelSize(20)
        
    def set_background_color(self, color):
        '''
        Sets background color to given QColor
        '''
        
        self.background_color = color
        self.background = QtGui.QBrush(self.background_color)
        
    def set_line_color(self, color):
        '''
        Sets force line color to given QColor
        '''
        
        self.line_color = color
        self.linePen = QtGui.QPen(color)
        
    def save(self):
        '''
        Saves settings to preferences-dictionary
        '''
        
        bc_dict = {}
        bc_dict['r'] = self.background_color.red()
        bc_dict['g'] = self.background_color.green()
        bc_dict['b'] = self.background_color.blue()
        
        lc_dict = {}
        lc_dict['r'] = self.line_color.red()
        lc_dict['g'] = self.line_color.green()
        lc_dict['b'] = self.line_color.blue()
        
        other = {}
        other['line_lenght'] = self.line_lenght
        other['draw_lines'] = self.draw_lines
        
        self.controller.pref_dict['background_color'] = bc_dict
        self.controller.pref_dict['line_color'] = lc_dict
        self.controller.pref_dict['helper'] = other
        
        
        #return (bc_dict, lc_dict, other)
        
    def load(self):
        '''
        Loads settings from preferences-dictionary
        '''
        if 'background_color' in self.controller.pref_dict:
            bc_dict = self.controller.pref_dict['background_color']
            background_color = QtGui.QColor(int(bc_dict['r']), int(bc_dict['g']), int(bc_dict['b']))
            self.set_background_color(background_color)
        
        if 'line_color' in self.controller.pref_dict:
            lc_dict = self.controller.pref_dict['line_color']
            line_color = QtGui.QColor(int(lc_dict['r']), int(lc_dict['g']), int(lc_dict['b']))
            self.set_line_color(line_color)
            
        if 'helper' in self.controller.pref_dict:
            other = self.controller.pref_dict['helper']
            line_lenght = other['line_lenght']
            
            self.line_lenght = int(line_lenght)
            
            draw_lines = other['draw_lines']
            
            if draw_lines == 'True':
                self.draw_lines = True
            if draw_lines == 'False':
                self.draw_lines = False
        
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
        Scales object locations for QPaint
        '''
        
        x =  uni_object.x - self.center_x
        y =  uni_object.y - self.center_y
        
        x = self.scale_factor * x
        y = self.scale_factor * y
        
        x = int(  + x )
        y = int(  - y )
        
        return ( x, y )
        
    def line_direction(self, x, y, size):
        '''
        get direction line endpoint
        '''
        r = self.controller.universe.maths.get_vector_lenght(x,y,0)
        
        if r == 0:
            return ( None, None )
        
        scale = ( self.line_lenght + size ) / r
        
        x = scale * x
        y = scale * y
        
        x = int(  + x )
        y = int(  - y )
        
        return ( x, y )
        

    def paint(self, painter, event):
        '''
        Paint objects and lines
        '''
        
        painter.fillRect(event.rect(), self.background)
        painter.translate(painter.device().width()/2, painter.device().height()/2)

        painter.save()
        
        for uni_object in self.controller.universe.object_list:
            
            ( x, y ) = self.scale(uni_object)
            point = QtCore.QPoint(x, y)
            size = uni_object.object_type# * 2
            
            if self.draw_lines:
                (fx, fy) = self.line_direction(uni_object.force_x, uni_object.force_y, size)
                if fx is not None:
                    painter.setPen(self.linePen)
                    f_line = QtCore.QPoint(x+fx, y+fy)
                    painter.drawLine(point, f_line)
            
            (r,g,b) = uni_object.color
            color = QtGui.QColor(r, g, b)
            painter.setBrush(color)
            painter.setPen(color)
            
            if self.draw_lines:
                (sx, sy) = self.line_direction(uni_object.speed_x, uni_object.speed_y, size)
                if sx is not None:
                    s_line = QtCore.QPoint(x+sx, y+sy)
                    painter.drawLine(point, s_line)
            
            painter.drawEllipse(point, size, size)
            
        painter.restore()
        
        painter.setPen(self.textPen)
        painter.setFont(self.textFont)
        time = self.controller.units.time.num(self.controller.universe.calc_time)
        text = str(round(time, 1)) + ' ' +  self.controller.units.time.unit
        painter.drawText(QtCore.QRect(self.width/2-100, self.height/2-100, 100, 100), 
                            QtCore.Qt.AlignCenter, text)
            

class Widget(QtGui.QWidget):
    '''
    QWidged where paint happens
    Code originally from:
    U{http://qt.gitorious.org/pyside/pyside-examples/blobs/e853ca94f7ccd122d3498fe562db5d28c4e37edb/examples/opengl/2dpainting.py}
    '''
    
    def __init__(self, helper, parent = None):
        QtGui.QWidget.__init__(self)
        
        self.helper = helper
        self.animating = False

    def animate(self):
        '''
        Runs simulation step and repaints
        '''
        self.animating = True
        
        for i in range(self.helper.controller.steps_between_paint):
            self.helper.controller.animate_step()
        
        self.repaint()
        self.animating = False

    def paintEvent(self, event):
        '''
        Event in painter
        '''
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        if self.animating is False:
            self.helper.width = painter.device().width()
            self.helper.height = painter.device().height()
            self.helper.get_scale_factor()
        
        self.helper.paint(painter, event)
        painter.end()
