#Using the sliding window technique using two pointers and a charset to keep track of unique characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        elif s==" ":
            return 1
        elif len(s)==1:
            return 1
        elif len(s)==2:
            if s[0]==s[1]:
                return 1
            else:
                return 2
        l=0
        r=1
        charSet = set()
        charSet.add(s[l])
        maxSize=0
        while r<len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l+=1
                charSet.add(s[r])
            r+=1
            if (len(charSet)>maxSize):
                maxSize=len(charSet)
            print(charSet)
        return maxSize
    

#Old Try

    # 
    # class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    # count=1 
    #     maxcount=0
    #     seen=[s[0]]
    #     # return len(set(s))
    #     # if s
    #     for i in range(len(s)-1):
    #         print(count,seen)
    #         if s[i+1] not in seen:
    #             count+=1
    #             seen.append(s[i+1])
    #         elif count>maxcount:
    #             maxcount=count
    #             seen=[]
    #             count=0
    #     return maxcount
