class Solution:
    def reverse(self, x: int) -> int:
        max = (2**31) -1
        reversedInt = 0
        while x != 0:
            digit = abs(x) % 10
            if x < 0: # if negative
                digit = -digit
            x = ((x - digit)// 10)

            if reversedInt > (max // 10): # over
                return 0
            if (reversedInt == (max // 10)) and (digit > 7): # over
                return 0
            if reversedInt < -214748364: # under
                return 0
            if (reversedInt == -214748364) and (digit < -8): # under
                return 0

            reversedInt = (reversedInt * 10) + digit
        return reversedInt



        