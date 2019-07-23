from drzewobinarne import BinaryTreeNode, BST

class RBNode(BinaryTreeNode):
    def __init__(self, s = 97, h = 53, data = None):
        BinaryTreeNode.__init__(self, s, h, data)
        self.__CR = 0
        self.__CB = 1
        self.__DB = 2
        self.__dict = {0: "red", 1: "black", 2: "double black"}
        self.__color = self.__CR
        
    @property
    def color(self):
        return self.__dict[self.__color]
    
    @color.setter
    def color(self, c):
        if c == self.__CR or c.lower() == "red":
            self.__color = self.__CR
        elif c == self.__CB or c.lower() == "black":
            self.__color = self.__CB
        elif c == self.__DB or c.lower() == "double black":
            self.__color = self.__DB
            
    def __repr__(self):
        return f'<{self.__dict[self.__color]} node with a key 0x{self.key.value:08x}>'
    
class RBT(BST):
    def __init__(self):
        sent = RBNode(data = "")
        sent.color = "black"
        BST.__init__(self, sent)

    def insert(self, node):
        x = BST.insert(self, node)
        if x is not node:
            return x
        x.color = "red"
        while x is not self.root and x.parent.color == "red":
            if x.parent is x.parent.parent.left:
                y = x.parent.parent.right
            else:
                y = x.parent.parent.left
            # przypadek 1
            if y.color == "red":
                y.color = "black"
                x.parent.color = "black"
                x.parent.parent.color = "red"
                x = x.parent.parent
                continue
            if x.parent is x.parent.parent.left: 
                # przypadek 2
                if x is x.parent.right:
                    self.rotate_left(x.parent)
                # przypadek 3
                x.color = "black"
                x.parent.color = "red"
                self.rotate_right(x.parent)
            else:
                if x is x.parent.left:
                    self.rotate_right(x.parent)
                x.color = "black"
                x.parent.color = "red"
                self.rotate_left(x.parent)
            break
        self.root.color = "black"
        return node
        
        