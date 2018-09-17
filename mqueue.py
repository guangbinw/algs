
class MQueue():

    def __init__(self,size = 16):
        self.array = list()
        for _ in range(size):
            self.array.append(None)
        
        self.size = size

        self.head = 0
        self.tail = 0

    def empty(self):
        return (self.head == self.tail)

    def full(self):
        val = 1 + self.tail - self.head
        return (val == 0) or (val == self.size) 
    
    def nextIdx(self,idx):
        nv = idx + 1
        if nv == self.size: # 代替取模操作
            nv = 0

        return nv

    def enqueue(self,v):
        if self.full(): #存储区满
            return False
        else: #存储区有空闲，队尾位置增加内容
            self.array[self.tail] = v
            self.tail = self.nextIdx(self.tail)

    def dequeue(self):
        if self.empty():
            return None
        else:
            v = self.array[self.head]
            self.head = self.nextIdx(self.head)

            return v
    
    def debug(self):
        print(self.array,self.head,self.tail)

if __name__ == '__main__':
    s = MQueue()
    s.enqueue(4)
    s.debug()

    v = s.dequeue()
    print(v)
    s.debug()
    
    v = s.dequeue()
    print(v)
    s.debug()
    
    s.enqueue(5)
    s.enqueue(6)
    s.debug()

    for i in range(24):
        s.enqueue(i)
        s.debug()

    for i in range(24):
        v = s.dequeue()
        print(v)
        s.debug()

    v = s.dequeue()
    print(v)
    s.debug()

    v = s.dequeue()
    print(v)
    s.debug()
