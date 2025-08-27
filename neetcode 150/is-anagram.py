class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for i in s:
            if i in a.keys():
                a[i]+=1
            else:
                a[i]=1
        
        for j in t:
            if j in b.keys():
                b[j]+=1
            else:
                b[j]=1

        if a == b:
            return True
        return False