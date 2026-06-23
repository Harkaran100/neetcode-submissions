class Solution:
    def minOperations(self, s: str) -> int:
        # there a re 2 possible answers for size n
        # start with 0 or start with 1 and alternate
        change_0 = 0
        change_1 = 0
        for i in range(len(s)):
            # even
            if i % 2 == 0:
                expected_start_0 = "0"
                expected_start_1 = "1"
            # odd
            else:
                expected_start_0 = "1"
                expected_start_1 = "0"
            if s[i] != expected_start_0:
                change_0 += 1
            if s[i] != expected_start_1:
                change_1 += 1
        

                # 010
        return min(change_0,change_1)
            





'''
        changes_start_0 = 0
        changes_start_1 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                expected_start_0 = "0"
                expected_start_1 = "1"
            else:
                expected_start_0 = "1"
                expected_start_1 = "0"

            if s[i] != expected_start_0:
                changes_start_0 += 1

            if s[i] != expected_start_1:
                changes_start_1 += 1

        return min(changes_start_0, changes_start_1)
'''
