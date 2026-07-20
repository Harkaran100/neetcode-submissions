class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # lens not same
        if len(s) != len(t):
            return False
        # create hashmap for each

        # hashmap for s
        s_map = {}
        for char in s:
            if char not in s_map:
                s_map[char] = 0
            s_map[char] += 1
        
        # hashmap for t
        t_map = {}
        for char in t:
            if char not in t_map:
                t_map[char] = 0
            t_map[char] += 1

        return t_map == s_map

        # time is o of s + n
        # space is o of a + b where a is unique in s and b is unique in t