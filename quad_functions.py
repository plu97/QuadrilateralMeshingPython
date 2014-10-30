
class Point(object):
    def __init__(self, name, input_x, input_y):
        self.name = name
        self.x = input_x
        self.y = input_y
        
    @classmethod
    def from_coordinates(cls, input_x, input_y):
        cls.x = input_x
        cls.y = input_y
        
class Line(object):
    def __init__(self, name, p1, p2):
        self.name = name
        self.point1 = p1
        self.point2 = p2
        

def cross_product(line1, line2):
    vector1x = line1.point2.x - line1.point1.x
    vector1y = line1.point2.y - line1.point1.y
    vector2x = line2.point2.x - line2.point1.x
    vector2y = line2.point2.y - line2.point1.y
    
    return vector1x*vector2y - vector1y*vector2x

def point_on_left_of_line(line1, point):
    return cross_product(line1, line(line1.point1, point)) > 0
