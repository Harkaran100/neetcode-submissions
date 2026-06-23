class Solution:
    def groupAnagrams(self, strs: List[str]):
        # use a hashset to count the number of chars in each string, then group by that

        # hashmap we will use
        result = {}

        # iterate though the strings
        for i in strs:
            count = [0] * 26 # to count instances of each lower case letter
            # somehow count everything in i
            for chars in i:
                count[ord(chars) - ord("a")] += 1
            key = tuple(count)

            if key not in result:
                result[key] = []
            result[key].append(i)
        
        return list(result.values())
            