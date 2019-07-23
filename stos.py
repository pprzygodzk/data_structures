from klasa import Element

class Stack:
    def __init__(self, maxSize):
        self.__items = [ None for i in range(maxSize) ]
        self.__max = maxSize
        self.__top = -1 # stos jest pusty, jak 0 to jeden element!
        
    @property
    def empty(self):
        return self.__top == -1
    
    @property
    def full(self):
        return self.__top == self.__max-1
    
    def push(self, e):
        if self.full:
            print("Stack overflowed!")
            return None
        self.__top += 1
        self.__items[self.__top] = e
        
    def pop(self):
        if self.empty:
            print("Stack is empty!")
            return None
        item = self.__items[self.__top]
        self.__top -= 1
        return item
    
    def __print__(self):
        for i in reversed(range(self.__top+1)):
            print(self.__items[i])