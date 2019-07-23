from klasa import Element

class BinaryTreeNode(Element):
    def __init__(self, s = 97, h = 53, data = None):
        Element.__init__(self, s, h, data)
        self.__right = None
        self.__left = None
        self.__parent = None
    
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, element):
        self.__right = element
    
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, element):
        self.__left = element
        
    @property
    def parent(self):
        return self.__parent
    
    @parent.setter
    def parent(self, element):
        self.__parent = element
        
class BST:
    def __init__(self, sent = None):
        self.__root = sent
        self.__sent = sent
    
    @property
    def root(self):
        return self.__root
        
    def insert(self, node):
        try:
            if self.__root is self.__sent:
                self.__root = node
                node.parent = self.__sent
                node.left = self.__sent
                node.right = self.__sent
                return node
            x = self.__root
            while x is not self.__sent:
                if node is x:
                    print("Node is already in the tree!")
                    return self.__sent
                y = x
                if node.key < x.key:
                    x = x.left
                else:
                    x = x.right
            node.parent = y
            node.left = self.__sent
            node.right = self.__sent
            if node.key < y.key:
                y.left = node
            else:
                y.right = node
            return node
        except:
            print("Bad node structure!")
            return self.__sent
        
    def search(self, key):
        x = self.__root
        while x is not self.__sent and x.key != key: # nie moze byc or, bo None.key by sprawdzilo
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def remove(self, node):
        z = node
        if z.left and z.right:
            z = self.successor(z)
        y = z.left if z.left else z.right
        if y:
            y.parent = z.parent
        if z.parent is self.__sent:
            self.__root = y
        else:
            if z.parent.left is z:
                z.parent.left = y
            else:
                z.parent.right = y
        if z is not node:
            node.data = z.data
        
    def inorder(self):
        self.__inorder(self.__root)
        
    def __inorder(self, node):
        if node is not self.__sent:
            self.__inorder(node.left)
            print(node)
            self.__inorder(node.right)
    
    def preorder(self):
        self.__preorder(self.__root)
    
    def __preorder(self, node):
        if node is not self.__sent:
            print(node)
            self.__preorder(node.left)
            self.__preorder(node.right)
            
    def postorder(self):
        self.__postorder(self.__root)
        
    def __postorder(self, node):
        if node is not self.__sent:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node)
            
    def successor(self, node):
        try:
            if node.right is not self.__sent:
                x = node.right
                while x.left is not self.__sent:
                    x = x.left
                return x
            x = node.parent
            while x is not self.__sent and x.right is node:
                node = x
                x = x.parent
            return x
        except:
            print('Node must be a BST node!')
            return self.__sent
        
    def rotate_right(self, y):
        x = y.left
        if x is self.__sent:
            return
        y.left = x.right
        if y.left is not self.__sent:
            y.left.parent = y
        x.right = y
        x.parent = y.parent
        y.parent = x
        if x.parent is self.__sent:
            self.__root = x
        else:
            if x.parent.left is y:
                x.parent.left = x
            else:
                x.parent.right = x
                
    def rotate_left(self, y):
        x = y.right
        if x is self.__sent:
            return
        y.right = x.left
        if y.right is not self.__sent:
            y.right.parent = x
        x.left = y
        x.parent = y.parent
        y.parent = x
        if x.parent is self.__sent:
            self.__root = x
        else:
            if x.parent.left is y:
                x.parent.left = x
            else:
                x.parent.right = x
            
        