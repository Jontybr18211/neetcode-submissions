class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        low,sums = 0,0
        for high in range(len(nums)):
            sums+=nums[high]
            while sums>=target:
                min_length = min(min_length,high-low+1)
                sums-=nums[low]
                low+=1
        return 0 if min_length==float('inf') else min_length