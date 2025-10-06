from typing import List

class Solution:
    def binarySearch(self,left,right,target,nums):
        print(nums[left:right])
        n=right-left
        if n==1:
            if nums[left:right]==[target]:
                return left
            else:
                return -1
        else:
            if n%2==0:
                t=left+int(n/2)
            else:
                t=left+int(n/2)
        print(nums[t],"f")
        if nums[t]>target:
            return self.binarySearch(left,t,target,nums)
        elif nums[t]<target:
            return self.binarySearch(t,right,target,nums)
        else:
            print("Jere")
            return t

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0,len(nums),target,nums)
    
print(Solution().search([-1,0,2,4,6,8],3))