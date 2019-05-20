# Let's Try It, page 390
class XYcoord(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    
    def __repr__(self):
        return '(' + str(self.__x) + ',' \
                    + str(self.__y) + ')'

coord = XYcoord(5, 2)
print(coord)
# OUT: (5,2)
str(coord)
# OUT: '(5,2)'
coord
# OUT: (5,2)