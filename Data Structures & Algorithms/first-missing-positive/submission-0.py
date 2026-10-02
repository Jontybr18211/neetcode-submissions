class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        mis=1
        for n in nums:
            if n>0 and n==mis:
                mis+=1
        return mis
