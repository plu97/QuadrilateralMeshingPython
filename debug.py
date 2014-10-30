from quad_functions import *

def debug():
    '''
        point1 = Point(5, 7)
        point2 = Point(3, 4)
        point3 = Point(2, 1)
        point4 = Point(7, 6)
        point5 = Point(2, 0)
        point6 = Point(5, 1)
        point7 = Point(3, 2)
        point8 = Point(1, 3)
        point9 = Point(0, 0)
        
        line1 = Line(point1, point2)
        line2 = Line(point3, point4)
        line3 = Line(point7, point8)
    '''
    
        
    point1 = Point(0, 0)
    point2 = Point(0, 6)
    point3 = Point(6, 0)
    point4 = Point(6, 6)
    point5 = Point(8, 3)
    
    point_set = [point1, point2, point3, point4]
    print gift_wrap(point_set)
    
    
        
    '''
    point_list = file_to_points(sys.argv[1])
    line_list = find_lines(point_list)
    print line_list
    '''