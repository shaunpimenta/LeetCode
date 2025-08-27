class Solution:
    # Using the ordinal trick and character freq for solving
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l={}
        for strr in strs:
            a=[0]*26
            for i in strr:
                a[ord(i)-ord('a')]+=1
            if str(a) in l.keys():
                l[str(a)].append(strr)
            else:
                l[str(a)]=[strr]
        return list(l.values())