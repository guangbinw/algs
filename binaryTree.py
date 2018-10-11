

class BTreeItem():

    def __init__(self,dat):
        self.dat = dat
        self.left = None
        self.right = None
        self.p = None
    
    def d_show(self):
        print(self.dat)

        l = self.left
        if l != None:
            l.show()
        
        r = self.right
        if r != None:
            r.show()
    
    def show(self):
        print(self.dat)

    def search(self,kval):
        if self.dat == kval:
            return self
        else:
            l = self.left
            if l != None:
                val = l.search(kval)
                if val != None:
                    return val
            
            r = self.right
            if r != None:
                val = r.search(kval)
                if val != None:
                    return val

        return None

class BinaryTree():

    def __init__(self):
        self.root = None

    def d_show(self):
        node = self.root
        if node != None:
            node.d_show()

    def w_show(self):
        cur = list()
        cur.append(self.root)
        
        while len(cur) > 0:
            childs = list()
            for node in cur:
                if node != None:
                    node.show()
                    childs.append(node.left)
                    childs.append(node.right)
            
            cur = childs

    def d_show_2(self):
        nodes = list()
        if self.root != None:
            nodes.append(self.root)

        while len(nodes) > 0:
            node = nodes[-1]
            nodes.pop()

            if node.right != None:
                nodes.append(node.right)
            
            node.show()

            if node.left != None:
                nodes.append(node.left)

    def addChild(self,node,child):
        if node == None:
            self.root = child

        if node.left == None:
            node.left = child
        elif node.right == None:
            node.right = child
        else:
            return None

        child.p = node
        return node
