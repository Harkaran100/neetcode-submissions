class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        left = 0
        right = 0
        s1Map = {}
        s2Map = {}
        #get s1 hashmap populated
        for i in range(window_len):
            if s1[i] not in s1Map:
                s1Map[s1[i]] = 0
            s1Map[s1[i]] += 1
        if window_len > len(s2):
            return False

        # populate s2 hashmap at start to window_len fix size
        while right < window_len:
            if s2[right] not in s2Map:
                s2Map[s2[right]] = 0
            s2Map[s2[right]] += 1
            right +=1

        if s2Map == s1Map:
            return True
        
        while right < len(s2):
            # by this point inital s2 window populated now we iterate through
            s2Map[s2[left]] -= 1
            if s2Map[s2[left]] == 0:
                del s2Map[s2[left]]
            left += 1
            
            if s2[right] not in s2Map:
                s2Map[s2[right]] = 0
            s2Map[s2[right]] += 1
            right +=1

            if s2Map == s1Map:
                return True

        return False

        