class MinStack:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        

    def push(self, val: int) -> None:
        if len(self.stack1)==0:
            self.stack1.append(val)
            self.stack2.append(val)
        else:
            self.stack1.append(val)
            minval=self.stack2[-1]
            if minval > val:
                self.stack2.append(val)  
            else:
                self.stack2.append(minval)      
        

    def pop(self) -> None:
        self.stack2.pop(-1)
        self.stack1.pop(-1)
        

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()