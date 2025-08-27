class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            if nums[i] in a.keys():
                a[nums[i]].append(i)
            else:
                a[nums[i]]=[i]
        for i in nums:
            if target-i in a.keys():
                if len(a[target-i])==1:
                    if a[target-i]!=a[i]:
                        return [a[i][0],a[target-i][0]]
                else:
                    return [a[i][0],a[target-i][1]]
