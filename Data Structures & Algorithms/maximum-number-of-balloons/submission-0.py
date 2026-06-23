class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # count char in baloon
        textmap = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }
        for i in text:
            if i in textmap:
                textmap[i] += 1
            else:
                continue
        return min(
            textmap["b"],
            textmap["a"],
            textmap["l"] // 2,
            textmap["o"] // 2,
            textmap["n"]
        )
        

        
        # make hashmap
        # make hashmap for input but only add the ballon letters and return minimum
        #o of n time
        #o of 1 size 

        