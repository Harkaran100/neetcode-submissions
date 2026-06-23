class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        result = [0] * length
        for i in range(length):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevDay = stack.pop()
                result[prevDay] = i - prevDay
            stack.append(i)
        return result
        