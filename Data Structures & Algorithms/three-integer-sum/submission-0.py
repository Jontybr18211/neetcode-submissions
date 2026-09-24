class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            target = nums[i] * -1
            while left<right:
                sums = nums[left] + nums[right]
                if sums==target:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<len(nums) and nums[left]==nums[left-1]:
                        left+=1
                    while right>=0 and nums[right]==nums[right+1]:
                        right-=1
                elif sums<target:
                    left+=1
                else:
                    right-=1
        return res