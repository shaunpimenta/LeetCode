class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lefts=[]
        rights=[]
        maxleft=0
        maxright=0
        for i in range(n):
            if i==0:
                lefts.append(0)
            elif height[i-1]>maxleft:
                maxleft=height[i-1]
                lefts.append(maxleft)
            else:
                lefts.append(maxleft)
        
        for i in range(n-1,-1,-1):
            if i==n-1:
                rights.append(0)
            elif height[i+1]>maxright:
                maxright=height[i+1]
                rights.append(maxright)
            else:
                rights.append(maxright)
        rights.reverse()
        mins=[]
        for l,r in zip(lefts,rights):
            mins.append(min(l,r))
        ans=[]
        for i in range(n):
            ans.append(mins[i]-height[i] if mins[i]-height[i]>0 else 0)
        return sum(ans)
    
#Optimized
class Solution:
    def trap(self, height: List[int]) -> int:
        l=1
        r=len(height)-1
        maxleft=height[0]
        maxright=height[-1]
        sumt=0
        while l<r:
            print(l,r,maxleft-height[l])
            sumt+=(maxleft-height[l] if maxleft-height[l]>0 else 0)
            # print(sumt)
            if height[l]>maxleft:
                maxleft=height[l]
                l+=1
            elif height[r]>maxright:
                maxright=height[r]
                r-=1
            else:
                l+=1
        return sumt