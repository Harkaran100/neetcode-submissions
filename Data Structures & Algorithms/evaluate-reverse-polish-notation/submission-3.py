class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # post fix solution
        #input is the 4 operands or str of int
        # 5 cases use a stack
        stack = []

        for i in tokens:

            if i == "+":
                temp = stack.pop() + stack.pop()
                stack.append(temp)
                
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b - a))
            
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b * a))

            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            
            # number
            else:
                stack.append(int(i))

        return stack[0]
        