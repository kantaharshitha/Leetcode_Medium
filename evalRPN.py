class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations='+-*/'
        for i in tokens:    
            if i in operations:
                num1=int(stack.pop(-1))
                num2=int(stack.pop(-1))
                if i == '+':
                    stack.append(num1+num2)
                elif i == '-':
                    stack.append(num2-num1)
                elif i == '*':
                    stack.append(num2*num1)
                elif i == '/':
                    stack.append(num2/num1)  
            else:
                stack.append(i)         
        return int(stack[-1])                     

