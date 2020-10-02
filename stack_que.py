# 3.1 Three in One:
#class Mulstack:

class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        self.stack.pop()

# 3.2 Stack Min:
class minstack:

    def __init__(self):
        self.stack = []
        self.minst = []

    def push(self, x):
        self.stack.append(x)
        if len(self.minst) == 0 or x<=self.minst[-1]:
            self.minst.append(x)
        
    def pop(self):
        k = self.stack.pop()
        if k == self.minst[-1]:
            self.minst.pop()

    def min_stack(self):
        return self.minst[-1]    
    
    def print(self):
        return self.stack

# 3.4 Queue using stack:

class quewst:

    def __init__(self):
        self.instack = []
        self.outstack = []
    
    def enqueue(self, x):
        self.instack.append(x)
    
    def dequeue(self):
        if len(self.outstack) == 0:
            while len(self.instack) != 0:
                self.outstack.append(self.instack.pop())
        
        return self.outstack.pop()


# 3.5 Sort Stack:

class sortstack:

    def __init__(self):
        self.stack = []
    
# 3.6 Animal Shelter

class animshel:
    
    def __init__(self):
        self.cat = []
        self.dog = []
        self.x = False
    
    def enqueue(self, animal:str, type:str):
        if type == "cat":
            self.cat.append(animal)
            self.x = True
        else:
            self.dog.append(animal)
            self.x = False
    
    def dequeueAny(self):
        if self.x == True:
            return self.cat.pop(0)
        else:
            return self.dog.pop(0)
    
    def dequeuedog(self):
        return self.dog.pop(0)
    
    def dequeuecat(self):
        return self.cat.pop(0)
    
    def print(self):
        print(self.cat)
        print(self.dog)


if __name__ == "__main__":

    x = minstack()
    x.push(39)
    x.push(23)
    x.push(4)
    x.push(9)
    x.push(7)
    x.push(11)
    print(x.min_stack())
    print(x.print())

    k = quewst()
    k.enqueue(1)
    k.enqueue(5)
    k.enqueue(4)
    k.enqueue(3)
    print(k.dequeue())

    m = animshel()
    m.enqueue('diego', 'dog')
    m.enqueue('shelly', 'cat')
    m.enqueue('dan', 'dog')
    m.enqueue('dww', 'cat')

    m.print()

    print(m.dequeueAny())





