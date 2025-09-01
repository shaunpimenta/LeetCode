class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        count = 1
        if nums==[]:
            return 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            elif nums[i]==nums[i+1]:
                continue
            else:
                if count > max_count:
                    max_count = count
                count =1
        if count > max_count:
            max_count = count
        return max_count