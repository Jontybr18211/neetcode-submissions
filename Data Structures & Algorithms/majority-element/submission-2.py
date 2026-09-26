class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        #val = 0
        for n in nums:
            if count==0:
                val=n
                count+=1
            else:
                count += (1 if val==n else -1)
        return val
