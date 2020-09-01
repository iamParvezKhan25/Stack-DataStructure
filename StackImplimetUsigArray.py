# Stack Data Structure Usig Array

class Stack:
    def __init__(self, size):
        self.stack = []
        self.top = 0
        self.size = size

    def push(self, newData):
        if self.size == self.top:
            print("ERROR : Stack is OVERFLOW!")
        else:
            self.stack.append(newData)
            self.top += 1
            print("Pushed in Stack : {}".format(newData))

    def pop(self):
        if self.top <= 0:
            print("ERROR : Stack is EMPTY!")
        else:
            exData = self.stack.pop()
            self.top -= 1
            print("Poped from Stack : {}".format(exData))

    def stackDisplay(self):
        print(":: Stack Display ::")
        for i in self.stack:
            print(i)

if __name__ =='__main__':

    s = Stack(5)# in Argument Declare Size/Capacity of Stack

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    s.push(60)
    s.stackDisplay()

    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.stackDisplay()
