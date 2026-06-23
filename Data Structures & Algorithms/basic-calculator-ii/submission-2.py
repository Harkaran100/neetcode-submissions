class Solution:
    def calculate(self, s: str) -> int:
        numStack = []
        operStack = []
        i = 0
        while i < (len(s)):
            if s[i] == " ":
                i+= 1
                continue
                # no need to i += 1 since its in range
            if s[i] == "+" or s[i] == "-":
                operStack.append(s[i])
                i += 1
            elif s[i] == "*" or s[i] == "/":
                oper = s[i]
                i += 1
                a = numStack.pop()

                # check if space after operator
                while i < len(s) and s[i] == " ":
                    i+= 1
                
                # build full number after operator
                b = 0
                while i < len(s) and s[i].isdigit():
                    b = b * 10 + int(s[i])
                    i += 1
                if oper == "*":
                    numStack.append(a * b) 
                else:
                    numStack.append(int(a / b)) 
            else:
                # its a number 
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                numStack.append(num)

        ans = numStack[0]
        for i in range(len(operStack)):
            oper = operStack[i]
            num = numStack[i + 1]

            if oper == "+":
                ans += num
            else:
                ans -= num

        return ans


