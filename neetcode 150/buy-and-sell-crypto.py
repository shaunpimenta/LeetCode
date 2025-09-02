class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        n=len(prices)
        maxprof=0
        while r!=n:
            prof=prices[r]-prices[l]
            if prof>maxprof:
                maxprof=prof
            if prices[l]>prices[l+1]:
                l+=1
                r+=1
            else:
                if prices[r]<prices[l]:
                    l=r
                r+=1
        return maxprof