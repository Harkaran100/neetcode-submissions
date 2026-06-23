class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        for i in path + "/":
            if i == "/":
                if curr == ".." and stack:
                    stack.pop()
                elif curr == ".." and not stack:
                    pass
                elif curr == ".":
                    pass
                elif curr != "":
                    stack.append(curr)
                curr = ""
            else:
                curr += i
        result =  "/" + "/".join(stack)
        return result

        