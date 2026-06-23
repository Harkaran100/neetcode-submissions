class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # input is 2 str
        # in order to even continue checking t >= s
        #if does not exist return return ""
        if len(t) > len(s):
            return ""

        # solve with 2 hashmaps
        t1 = {} # what we are checking for
        s1 = {}

        # min_string, left vars, min_len
        min_string = ""
        left = 0
        min_len = int(1001)

    

        # populate t1 hashmap
        for char in t:
            if char not in t1: # init that key 
                t1[char] = 0
            t1[char] += 1
        # create function to check if t1 in s1
        def check_subset():
            for i in t1:
                if i not in s1 or t1[i] > s1[i]:
                    return False
            return True
        
        for right in range(len(s)):
            # add right to s1
            if s[right] not in s1: # init that key 
                s1[s[right]] = 0
            s1[s[right]] += 1

            # check if t1 in s1
            is_subset = check_subset()
            
            # update min string
            while is_subset:
                if len(s[left:right + 1:]) <= min_len:
                    min_string = str(s[left:right + 1:])
                    min_len = len(s[left:right + 1:])

                # shrink process
                s1[s[left]] -= 1
                if s1[s[left]] == 0:
                    del s1[s[left]]
                left += 1

                is_subset = check_subset()
        return min_string
            
        # create algo dynamic sliding window using t1 hashmap
        # check if t1 hashmap in s1
        # s = "OUZODYXAZV", t = "XYZ"
        # left  = 0
        # for right in range
        # if right not in s1 add
        # check if t1 in s1
        # if not continue else store current substring in another var called min_string
        # then move left up 1 and check if t1 in s1
        # if not continue else store current substring in another var called min_string

