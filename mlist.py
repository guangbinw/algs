
class MItem():

    def __init__(self,dat):
        self.dat = dat
        self.pre = None
        self.next = None


class MList():

    def __init__(self):
        item = MItem(None)
        item.next = item
        item.pre = item
        self.nil = item

    def search(self,kval):
        x = self.nil.next
        while x != self.nil and x.dat != kval:
            x = x.next

        return x

    def delete(self,x):
        x.pre.next = x.next
        x.next.pre = x.pre

    def deleteVal(self,v):
        x = self.nil.next
        while x != self.nil:
            if x.dat == v:
                self.delete(x)
            x = x.next

    def insert(self,x):
        self.nil.next.pre = x
        x.next = self.nil.next
        self.nil.next = x
        x.pre = self.nil
    
    def debug(self):
        p = self.nil.next
        vals = list()
        while p != self.nil:
            vals.append(p.dat)
            p = p.next
        
        print(vals)

if __name__ == '__main__':
    s = MList()
    s.debug()
    
    x = MItem(5)
    s.insert(x)
    s.debug()
    
    x = MItem(6)
    s.insert(x)
    x = MItem(7)
    s.insert(x)
    s.debug()

    s.deleteVal(5)
    s.debug()

    for i in range(24):
        x = MItem(i)
        s.insert(x)

    s.debug()
