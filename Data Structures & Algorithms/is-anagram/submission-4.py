class Solution:
    # the way to solve this that comes to mind is using a hashset, the reason being
    # in hashset we can store key and value pairs, so we can count the number of
    # same characters used in s and t. if we do that and at end compare hashmaps of both
    # if = its a anagram otherwise it is not.
    def isAnagram(self, s: str, t: str):
        # create both hashmaps
        s_hashmap = {}
        t_hashmap = {}
        for i in s:
            if i in s_hashmap:
                s_hashmap[i] += 1
            else:
                s_hashmap[i] = 1
        for i in t:
            if i in t_hashmap:
                t_hashmap[i] += 1
            else:
                t_hashmap[i] = 1
        if s_hashmap == t_hashmap:
            return True
        return False
        # time complexity is o of n for each hashmap construction so worst case o of n simplfied
        # space complexoty is o of 1 since max 26 chars

    
        


