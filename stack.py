
class Stack():

    def __init__(self):
        self.array = list()
        self.size = 0
        self.top = 0

    def empty(self):
        return (self.top == 0)
    
    def push(self,v):
        if self.top >= self.size: #存储区满，append
            self.array.append(v)
            self.size = self.size + 1
        else: #存储区有空闲，在列表当前位置增加内容
            self.array[self.top] = v
        
        self.top = self.top + 1

    def pop(self):
        if self.empty():
            return None
        else:
            self.top = self.top - 1
            return self.array[self.top]
    
    def debug(self):
        print(self.array,self.top,self.size)

if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.debug()

    v = s.pop()
    print(v)
    s.debug()

    v = s.pop()
    print(v)
    s.debug()

    s.push(5)
    s.push(6)
    s.debug()

    v = s.pop()
    print(v)
    s.debug()

    v = s.pop()
    print(v)
    s.debug()
