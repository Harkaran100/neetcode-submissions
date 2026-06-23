class Solution:
    def isAnagram(self, s: str, t: str):
        dict_s = {}
        dict_t = {}
        i = 0
        while i < len(s):
            ch = s[i]
            if ch not in dict_s:
                #make it a key and set value count to 1
                dict_s[ch] = 1

            elif ch in dict_s:
                #increment its value counter by 1
                dict_s[ch] +=1
            # move onto next posotion in string
            i+= 1
        a = 0
        while a < len(t):
            ch = t[a]
            if ch not in dict_t:
                #make it a key and set value count to 1
                dict_t[ch] = 1

            elif ch in dict_t:
                #increment its value counter by 1
                dict_t[ch] +=1
            # move onto next posotion in string
            a+= 1
        return dict_s == dict_t
    
        


