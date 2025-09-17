class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Using prefix and postfix arrays
        #O(n) time and O(n) space
        #Calculate the multiplication of all elements to the left of each index and store in prefix array
        #Calculate the multiplication of all elements to the right of each index and store in postfix array
        #Dividing the product by the element at that index gives the product of array except self does not work with 0s 
        #hence we use prefix and postfix arrays

        prefix=[1]
        postfix=[1]
        t=0
        for i in nums:
            prefix.append(i*prefix[t])
            t+=1
        t=0
        for i in nums[::-1]:
            postfix.append(i*postfix[t])
            t+=1
        postfix=postfix[::-1]
        print(prefix,postfix)
        ans=[]
        for i in range(1,len(nums)+1):
            ans.append(prefix[i-1]*postfix[i])
        return ans

        #O(n) time and O(1) space
        ans=[1]
        t=0
        for i in range(0,len(nums)-1):
            print(ans)
            ans.append(nums[i]*ans[-1])
        prod=1
        print(ans)
        for i in range(len(nums)-2,-1,-1):
            prod*=nums[i+1]
            print(prod)
            ans[i]*=prod
        return ans