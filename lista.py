from klasa import Element
from klasa import Key

class ListElement(Element):
    def __init__(self, s = 97, h = 53, data = None):
        Element.__init__(self, s, h, data)
        self.__right = None
        
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, next_element):
        self.__right = next_element
        
class List:
    def __init__(self):
        self.__head = None
        
    def insert(self, e):
        try:
            e.right = self.__head
            self.__head = e
            return self.__head
        except:
            print('Element must have a field named \'right\'')
            return None
        
    @property
    def items(self):
        _list = []
        x = self.__head
        while x is not None:
            _list.append(x)
            x = x.right
        return _list
    
    def delete(self, e):
        x = self.__head
        while x is not None and x.key != e.key:
            prev = x
            x = x.right
        if x.key == e.key:
            prev.right = x.right
    # a is b b = search na wypadek gdyby 2 byly takie same
    
    def search(self, key):
        x = self.__head
        while x is not None and x.key != key:
            x = x.right
        return x    
        
    