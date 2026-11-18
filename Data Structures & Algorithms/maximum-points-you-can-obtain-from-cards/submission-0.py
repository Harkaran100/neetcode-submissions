class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = (len(cardPoints) - 1) - k
        currentPoints = sum(cardPoints[right + 1:])
        maxPoints = currentPoints
        for i in range(right + 1, len(cardPoints)):
            currentPoints += cardPoints[left] - cardPoints[i]
            left += 1
            maxPoints = max(maxPoints,currentPoints)
        return maxPoints
        