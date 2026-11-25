class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        goal={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in goal:
                return [goal[diff],i]
            goal[num]=i