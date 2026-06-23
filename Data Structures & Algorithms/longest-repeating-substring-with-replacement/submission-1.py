class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        hashmap = {}
        longestSubString = 0
        #main loop to make sure we go through everything
        while right < len(s):
            # 1) add current right character into hashmap
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] +=1
            # 2) max repeated in hashmap
            most_freq = max(hashmap.values())
            #check if string is not valid
            while (right - left + 1) - most_freq > k: #not valid
                hashmap[s[left]] -=1
                left +=1
            currentSubString = right - left +1
            longestSubString = max(longestSubString, currentSubString)
            right +=1

        return longestSubString



        
        
        # given string s
        # whats longest substring i can make of repeating chars with k replacements
        # since comparing / going through a string, I am thinking of a two pointer, sliding window solution
        # also to check whats in current substring use hashmap

        # check if current sub is valid or not

        #if valid calculate len , increment right +=1, to avoid out of bound edge case check if r+=1 exists
        # add +=1 new right to hashmap
        # after calculating len compare with longest

        #if not valid, dont calculate len, decrement left in hashmap
        # increment left +=1

        