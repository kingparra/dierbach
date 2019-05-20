# Let's Try It, page 389
class SomeClass(object):
    def __init__(self):
        self.__n = 0
        self.n2 = 0
        

obj = SomeClass()
obj.__n
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT:     obj.__n
# OUT: AttributeError: 'SomeClass' object has no attribute '__n'
obj._SomeClass__n
# OUT: 0
obj.n2
# OUT: 0