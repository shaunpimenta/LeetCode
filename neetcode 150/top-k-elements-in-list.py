class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        for i in nums:
            if i in a.keys():
                a[i]+=1
            else:
                a[i]=1
        aa = list(a.values())
        aa.sort(reverse=True)
        t = aa[:k]
        ans = []
        for key,val in a.items():
            if val in t:
                ans.append(key)
        return ans