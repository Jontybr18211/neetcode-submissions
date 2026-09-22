class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pref=1
        for n in range(len(nums)):
            res[n]=pref
            pref*=nums[n]
        suff=1
        for n in range(len(nums)-1,-1,-1):
            res[n]*=suff
            suff*=nums[n]
        return res