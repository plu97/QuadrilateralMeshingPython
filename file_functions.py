import re, quad_functions

def file_to_points(file_name):
    file = open(file_name, 'r')
    point_list = []
    
    for line in file:
        match = re.match('(\d+)\s*\(\s*(\d+),\s*(\d+)\s*\)', line)
        if match:
            point_to_add = point(match.group(1), match.group(2), match.group(3))
            point_list.append(point_to_add)
    
    close(file_name)
    
    return point_list