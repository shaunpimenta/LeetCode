#Reduce the problem to finding anagrams in a string
#Time complexity: O(26n) where n is length of s2 and m is 26
#Use sliding window technique and hashmaps to store frequency of characters


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sd1=dict()
        for i in s1:
            if i in sd1:
                sd1[i]+=1
            else:
                sd1[i]=1
        
        l=0
        r=len(s1)-1
        while r<len(s2):
            sd2=dict()
            for i in range(l,r+1):
                if s2[i] in sd2:
                    sd2[s2[i]]+=1
                else:
                    sd2[s2[i]]=1
            if sd1==sd2:
                return True
            l+=1
            r+=1
        return False

#Optimized approach
#Time complexity: O(n) where n is length of s2
