class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input array of strs, group all anagrams into sublists

        # anagram has same frequency of letters

        # if i sort the words where to store that will be o of n space

        # go through once see if a sorted verison if str exsits as key if not make sorted the key and the value append as val, do throughout
        # this way we can sort anagrams by there sorted strs.  this will be o of n x klogn? not sure of this explIN
        # SPACE O OF u where u in unique anagrams

        group_str = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in group_str:
                group_str[sorted_str] = []
            group_str[sorted_str].append(string)
        return(list(group_str.values()))
            
        