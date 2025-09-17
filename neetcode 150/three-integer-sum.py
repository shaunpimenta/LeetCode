
#We first reduce the problem to a 2-sum problem by fixing one element and then using two pointers to find the other two elements that sum to the negative of the fixed element.
#Currently finding a more optimized solution
# Currently takes O(n^2) time and O(n) space

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=set()
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                sumt=nums[i]+nums[l]+nums[r]
                if sumt==0:
                    ans.add((nums[i],nums[l],nums[r]))    
                    r-=1
                elif sumt>0:
                    r-=1
                else:
                    l+=1
        return list(ans)
        
print(Solution().threeSum([-1,0,1,2,-1,-4]))