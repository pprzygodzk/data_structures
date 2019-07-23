from random import randint
import string

class Key:
    def __init__(self, key = None):
        self.value = key
        
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, key):
        try:
            self.__value = None if key is None else int(key)
        except:
            print("Error: Improper value!")
    
    def __eq__(self, k):
        return self.value == k.value
    
    def __gt__(self, k):
        return self.value > k.value
    
    def __lt__(self, k):
        return self.value < k.value
    
    def add_keys(self, k):
        self.value += k.value
        k.value = None
        
    def subst_keys(self, k):
        if self.__gt__(k):
            self.value -= k.value
            k.value = None
        elif self.__eq__(k):
            self.value = 0
            k.value = None
        elif self.__lt__(k):
            print("Values must be natural numbers!")
            
    def mult_keys(self, k):
        self.value *= k.value
        k.value = None
        
    def div_keys(self, k):
        if self.__lt__(k):
            print("Values must be natural numbers!")
        elif self.__eq__(k):
            self.value = 1
            k.value = None
        elif self.__gt__(k) and self.value % k.value == 0:
            self.value /= k.value
            k.value = None
        else:
            print("Values must be natural numbers!") 
    
    def __repr__(self):
        return str(self.value)


class Element:
    def __init__(self, s = 97, h = 53, data = None):
        self.__s = s
        self.__h = h
        self.__data = data
        if data is None:
            self.__data = ''.join([ chr(randint(33,126)) for i in range(4096) ])
            # od wykrzyknika 33 do 126 bez delete 127
        self.__genkey()
            
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, owndata):
        self.__data = owndata
        self.__genkey()
    
    @property
    def key(self):
        return self.__key
    
    def __repr__(self):
        # return f'<Element with a key 0x{self.__key.value:08x}>'
        return '<Element with a key 0x{:08x}>'.format(self.key.value) # 0 to indeks od 0
    # 04d to 4 miejsca zawsze wypelnione zerami jesli puste np. 0003
    
    def __eq__(self, e):
        return self.key.value == e.key.value
    
    def __gt__(self, e):
        return self.key.value > e.key.value
    
    def __lt__(self, e):
        return self.key.value < e.key.value
    
    def __genkey(self):
        k = 0
        for d in self.data:
            k = (k*self.__s+ord(d)) % self.__h # ord odwrotna do chr (char)
        self.__key = Key(k)