import random

class Q1114():

    def __init__(self,num):
        self.stack = [v for v in range(num)]
        self.hash = [random.randint(9,9 + v) for v in range(num)]
        self.num = num
        self.count = 0

    def search(self,val):
        if val > self.num:
            return None
        
        p = self.hash[val]
        if p >= 0 and p < self.count and self.stack[p] == val:
            return p
        
        return None

    def add(self,v):
        if v > self.num:
            return None
        
        ret = self.search(v)
        if ret != None:
            return None
        
        self.hash[v] = self.count
        self.stack[self.count] = v
        self.count += 1

        return self.count
    
    def delv(self,v):
        if v > self.num:
            return None
        
        ret = self.search(v)
        if ret == None:
            return None
        
        self.count -= 1
        pre =  self.stack[self.count]
        self.stack[ret] = pre
        self.hash[pre] = ret

        return ret

    def debug(self):
        print(self.stack,self.hash,self.count)


if __name__ == '__main__':
    q = Q1114(16)

    q.add(5)
    q.debug()
    q.search(5)
    q.debug()

    q.add(6)
    q.debug()
    q.add(5)
    q.debug()

    q.add(8)
    q.debug()
    q.add(2)
    q.debug()

    q.delv(5)
    q.debug()

