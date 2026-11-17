class Solution:
    def longestPalindrome(self, s: str) -> str:
        # what if for every str, I build outword
        #o of n2 so while there is left and right and they are same continue
        # at each iteration comapre with maxLen so far if greater save this as ans and update maxLen
        # this is also o of l space where l is longest substring
        # however this case should work for substrings with 1 mid value of 2 then how to go about it?

        maxLen = 0
        longestSub = ""
        for i in range(len(s)):
            left = i
            right = i
            # check mid case (bab)
            while 0 <= left <= right < len(s):
                if s[left] == s[right]:
                    if (right - left + 1) > maxLen:
                        maxLen = right - left + 1
                        longestSub = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break # ends while loop
            left = i
            right = i + 1
            # check mid case (bab)
            while 0 <= left <= right < len(s):
                if s[left] == s[right]:
                    if (right - left + 1) > maxLen:
                        maxLen = right - left + 1
                        longestSub = s[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break # ends while loop
        return longestSub

            

            #check double mid case (abba)
       