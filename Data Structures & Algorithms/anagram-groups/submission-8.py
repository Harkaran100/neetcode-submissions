class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap where k is populated alphanumeric values counts since only lowercase 
        # Use this as key and append values with same key

        group_anagrams = {}
        for string in strs:
            asciiCount = [0] * 26
            for char in string:
                count = ord(char) - ord("a")
                asciiCount[count] += 1
            tup_ascii_count = tuple(asciiCount)
            if tup_ascii_count not in group_anagrams:
                group_anagrams[tup_ascii_count] = []
            group_anagrams[tup_ascii_count].append(string)
        return (list(group_anagrams.values()))
