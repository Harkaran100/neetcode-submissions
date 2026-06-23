class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        result = [0] * length

        for i in range(length):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevday = stack.pop()
                result[prevday] = i - prevday
            stack.append(i)
        return result