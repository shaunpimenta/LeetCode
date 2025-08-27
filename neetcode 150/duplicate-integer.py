class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a={}
        for i in nums:
            if i in a.keys():
                return True
            else:
                a[i]=1
        return False
        