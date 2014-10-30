import re, struct

class point(object):
    def __init__(self, name = ' ', input_x, input_y):
        self.name = name
        self.x = input_x
        self.y = input_y
    
    
class line(object):
    def __init(self, name = ' ', p1 = point(), p2 = point()):
        self.name = name
        self.point1 = point()
        self.point2 = point()

    
def cross_product(line1, line2):
    vector1x = line1.point2.x - line1.point1.x
    vector1y = line1.point2.y - line1.point1.y
    vector2x = line2.point2.x - line2.point2.x
    vector2y = line2.point2.y - line2.point2.y
    
    return vector1x*vector2y - vector1y*vector2x

def point_on_left_of_line(line1, point):
    return cross_product(line1, line(line1.point1, point)) > 0

def find_lines(point_list):
    sorted_point_list = sorted(point_list)
    point_on_hull = sorted_point_list[0]
    endpoint = sorted_point_list[0]
    hull_point_list = []
    line_list = []
    i = 0
    
    while not endpoint == hull_point_list[0]:
        hull_point_list[i] = point_on_hull
        endpoint = sorted_point_list[0]
        
        for j in range(1, length(point_list)):
            
            on_left = point_on_left_of_line(line(hull_point_list[i], endpoint), sorted_point_list[j])
            if endpoint == point_on_hull or on_left:
                endpoint = sorted_point_list[j]
                
        i += 1
        line_to_add = line(point_on_hull, endpoint)
        line_list.append(line_to_add)
        point_on_hull = endpoint
        
        return line_list
        


#input: list of point struct
'''
class find_lines(point_list):
    line_list = []
    point_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}
    
    sorted_point_list = sorted(point_list, key = lambda point:point.x)
    
    if sorted_point_list[0].x == sorted_pointlist[1].x:
        
        if sorted_point_list[0].y > sorted_point_list[1].y:
            origin = 0
            low_point = 1
        else:
            high_point = 1
            low_point = 0
        
        line_name = sorted_point_list[origin].name + sorted_point_list[second].name
        line_list.append(line_name)
        
        if sorted_point_list[2].y > sorted_point_list[3].y:
            high_point = 2
            low_point = 3
        else: 
            high_point = 3
            low_point = 2
            
        line_name = sorted_point_list[1].name + sorted_point_list[high_point].name
        line_list.append(line_name)
        
        line_name = sorted_point_list[high_point].name + sorted_point_list[low_point].name
        line_list.append(line_name)
        
        line_name = sorted_point_list[low_point].name +
        
    
    elif sorted_point_list[1].y > sorted_point_list[2].y:
        line_list.append()

class find_lines(read_file_name, write_file_name):
    rf = open(read_file_name, 'r')
    point_set = []
    point_dict = {0: 'A', 1: 'B', 2:'C', 3:'D'}
    i = 0

    for line in rf:
        match = re.match('\(\s*(\d+),\s*(\d+)\s*\)', line)
        if match:
            p0 = point()
            p0.x = match.group(1)
            p0.y = match.group(2)
            
            point_set[i] = (i, match.group(1), match.group(2))
        i += 1
        
    point_set = sorted(point_set, key = lambda point:point[1])
    wf = open(write_file_name, 'w')
    
    if point_set[1][2] > point_set
    
    wf.write(str(point_set[0]) + str(point_set[1]) + ' ')
    wf.write(str(point_set[1]) + str(point_set[3]) + ' ')
    
    wf.write(str(point_set[0]) + str(point_set[2]) + ' ')

'''
        
    