
class Point(object):
    def __init__(self, input_x, input_y):
        self.x = input_x
        self.y = input_y
        
    def __str__(self):
        return "Point object with x = " + str(self.x) + " and y = " + str(self.y)
        
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        

class Line(object):
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2
    
    def __str__(self):
        string = "Line object with Point (" + str(self.point1.x) + "," + str(self.point1.y) + ")"
        string += "\nand Point (" + str(self.point2.x) + "," + str(self.point2.y) + ")"
        return string

    def __repr__(self):
        string = "(" + str(self.point1.x) + "," +str(self.point1.y) + ")"
        string += " and (" + str(self.point2.x) + "," + str(self.point2.y) + ")"
        return string

    def __eq__(self, other):
        return self.point1 == other.point1 and self.point2 == other.point2


def cross_product(line1, line2):
    vector1x = line1.point2.x - line1.point1.x
    vector1y = line1.point2.y - line1.point1.y
    vector2x = line2.point2.x - line2.point1.x
    vector2y = line2.point2.y - line2.point1.y
    
    return vector1x*vector2y - vector1y*vector2x

def point_on_left_of_line(point, line):
    return cross_product(line, Line(line.point1, point)) > 0

def gift_wrap(point_list):
    sorted_list = sorted(point_list, key = lambda point: point.x)
    polygon = list()
    initPoint = sorted_list[0]
    
    while len(polygon) == 0 or polygon[len(polygon) - 1].point2 != initPoint:
        '''
        if len(polygon) == 0: 
            print sorted_list[0]
        else:
            print polygon[len(polygon) - 1].point2
        '''
        
        if len(sorted_list) == 1: 
            finalLine = Line(sorted_list[0], initPoint)
            polygon.append(finalLine)
            break
        
        if len(polygon) == 0:
            startingPoint = sorted_list[0]
        else:    
            startingPoint = polygon[-1].point2

        
        sorted_list.remove(startingPoint)
        tentativeLine = Line(startingPoint, sorted_list[0])
        num = 0    

        
        '''    
        if len(sorted_list) == 2:
            tentativeLine = Line(startingPoint, sorted_list[1])
            if point_on_left_of_line(initPoint, tentativeLine):
                lastLine = Line(startingPoint, initPoint)
                polygon.append(lastLine)
                
            else:
                penultLine = Line(startingPoint, sorted_list[1])
                lastLine = Line(sorted_list[1], initPoint)
                polygon.append(penultLine)
                polygon.append(lastLine)
                
            print "BRGH"
            break
        '''
                
            
        for i in range(1, len(sorted_list)):
            if sorted_list[i] == startingPoint:
                continue
            if point_on_left_of_line(sorted_list[i], tentativeLine):
                tentativeLine = Line(startingPoint, sorted_list[i])
                num = i
                
        polygon.append(tentativeLine)
            
    
    return polygon

def reorient_quad(line_list):
    return_list = []

    for line in reversed(line_list):
        return_list.append(Line(line.point2, line.point1))
    return_list.append(return_list.pop(0))


    return return_list

def deconstruct_quad(line_list):
    point_list = list()
    for line in line_list:
        point_list.append(line.point1)
        
    return point_list


def aspect_ratio(point_list):
    #refer to CRE method of element testing paper for formula
    #equation 8 and 11 to be exact

    e2 = 0.0
    e2 += point_list[1].x + point_list[2].x
    e2 -= point_list[0].x + point_list[3].x
    e2 /= 4
    f3 = 0.0
    f3 += point_list[2].y + point_list[3].y
    f3 -= point_list[0].y + point_list[1].y
    f3 /= 4

    return max(e2/f3, f3/e2)

def skew(point_list):
    #refer to CRE method of element testing paper for formula
    #equation 8 and 12

    e3 = 0.0
    e3 += point_list[2].x + point_list[3].x
    e3 -= point_list[0].x + point_list[1].x
    f3 = 0.0
    f3 += point_list[2].y + point_list[3].y
    f3 -= point_list[0].y + point_list[1].y

    return e3/(f3*4)



