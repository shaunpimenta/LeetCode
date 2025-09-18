class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=1
        t=k
        count=1
        maxcount=1
        charSet=set()
        for i in s:
            charSet.add(i)
        for st in charSet:
            maxcount=max(maxcount,count)
            l=0
            r=0
            count=0
            t=k
            while r<len(s):
                if st==s[r]:
                    r+=1
                    count+=1
                else:
                    if t>0 and k>0:
                        t-=1
                        count+=1
                        r+=1
                    elif k==0:
                        maxcount=max(maxcount,count)
                        l=r
                        r+=1
                        count=0
                    else:
                        maxcount=max(maxcount,count)
                        while l<r and t<=0:
                            if s[l]!=st:
                                t+=1
                            l+=1
                            count-=1
        return max(maxcount,count)

print(Solution().characterReplacement("AAAAABBBBCBB",3))