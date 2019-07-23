from klasa import Element

MAX_QUEUE_SIZE = 10000

class Queue:
    def __init__(self, maxSize):
        self.__size = MAX_QUEUE_SIZE if maxSize > MAX_QUEUE_SIZE else maxSize
        if maxSize > MAX_QUEUE_SIZE:
            maxSize = MAX_QUEUE_SIZE
        self.__items = [ None for i in range(self.__size) ]
        self.__max = maxSize
        self.__head = 0
        self.__tail = 0
        
    @property
    def empty(self):
        return self.__head == self.__tail
    
    @property
    def full(self):
        return self.__head == (self.__tail + 1) % self.__size
        # (t+1) % n = h bo (n-1+1) % n = 0 = h, tj. zawracanie indeksu
    
    @property # zeby bylo bez nawiasu, ulatwienie
    def items(self):
        if self.__head <= self.__tail: # nie ma zawracania
            return self.__items[self.__head:self.__tail]
        return self.__items[self.__head:] + self.__items[:self.__tail] #zawracanie
    
    def enqueue(self, e):
        if self.full:
            print('Queue overflowed!')
            return None
        self.__items[self.__tail] = e
        self.__tail = (self.__tail + 1) % self.__size
        # (t+1)%n wszystko t+1 jezeli mniejsze niz n, a jak rowne n to t = 0
        return e
    
    def dequeue(self):
        if self.empty:
            print('Queue\'s empty!')
            return None
        e = self.__items[self.__head]
        self.__head = (self.__head + 1) % self.__size
        return e
    
    def __repr__(self):
        return '\n'.join([str(item) for item in self.items])
    
    def printq(self):
        for i in range(self.__head, self.__tail+1):
            print(self.__items[i])