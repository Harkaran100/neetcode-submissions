# ignores spaces only looks at letters and numbers
# can solve this with 2 pointers one at start one at end they walk inwards 
#(start pointers walks right and end pointer walks left

# how to filter out all non alphanumerics
# how to account for case where it is odd numbers
# even = "Haah" stops in even case last before crossover can tell if true or false
# odd = "lol" in order for this to be acconted true at some point left and right counter
# must be on same character
# so we can keep going until they left and right cross each other
#maybe use ascii

class Solution:
    def isPalindrome(self, s: str):
        # set L to first char, set R to last char
        leftPointer = 0 #first element
        rightPointer = (len(s) - 1) # last element

        while leftPointer <= rightPointer:
            #skip non alphahumeric
            while leftPointer <= rightPointer and not self.isAlphaNumeric(s[leftPointer]):
                leftPointer += 1
            while leftPointer <= rightPointer and not self.isAlphaNumeric(s[rightPointer]):
                rightPointer -= 1
            # Now at alphamuerics if not match
            if leftPointer <= rightPointer and s[leftPointer].lower() != s[rightPointer].lower():
                return False
            # increment

            leftPointer +=1
            rightPointer -=1
        return True
            
    
    # create function to see if alphanumeric
    def isAlphaNumeric(self,char):
        if ord("A") <= ord(char) <= ord("Z") or ord("a") <= ord(char) <= ord("z") or ord("0") <= ord(char) <= ord("9"):
            return True
        return False
