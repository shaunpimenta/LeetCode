from typing import List

#Semi Brute Force 31 / 48 testcases passed Leetcode
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=0
        r=1
        ans=[]
        t=0
        zerc=True
        while l<len(temperatures)-1:
            print(l,r)
            if r<len(temperatures) and temperatures[l]<temperatures[r]:
                print(temperatures[l],temperatures[r])
                t=r-l
                ans.append(t)
                l+=1
                r=l
                zeroc=False
            if r>len(temperatures)-1:
                r=l
                l+=1
                ans.append(0)
                zeroc=True
                t=0
            r+=1
        ans.append(0)
        return ans
    
#Optimized O(n) space O(n)
#Uses Monotonic Stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            t=temperatures[i]
            if stack==[]:
                stack.append((t,i))
            elif stack[-1][0]<t:
                while stack!=[] and stack[-1][0]<t:
                    a=stack.pop(-1)
                    ans[a[1]]=i-a[1]
                stack.append((t,i))
            else:
                stack.append((t,i))
        return ans
                
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))

#More Optimized
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        ans=[0]*n
        for i in range(n):
            while (stack!=[] and temperatures[i] > temperatures[stack[-1]]):
                ind = stack.pop(-1); 
                ans[ind] = i - ind
            stack.append(i)
        return ans
