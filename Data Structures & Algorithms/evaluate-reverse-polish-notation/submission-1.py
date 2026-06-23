class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-","*","/"]
        stack = []

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    res = b + a
                    stack.append(res)
                elif i == "-":
                    res = b - a
                    stack.append(res)
                elif i == "*":
                    res = b * a
                    stack.append(res)
                else:
                    res = int(b / a)
                    stack.append(res)
                
        # return res
        return stack[-1]




        # push if not oper
        #  if we get operator pop 2 times
        #
        # [+,2,1] once this is in stack compute tokens[-1][operator][token[-2]]
        #update res with that, push res
        # then continue itterating for i in range tokens
        # return res at the very end.

        # how to get operator from string to real artehmtic?
        # hashmap?
        #operatorMap = {"+": +, "-": -, "*": *, "/": /}
        