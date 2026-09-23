class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j=0,len(nums)-1
        res = [0]*len(nums)
        for k in range(len(nums)-1,-1,-1):
            if abs(nums[i])>abs(nums[j]):
                res[k]=nums[i]*nums[i]
                i+=1
            else:
                res[k]=nums[j]*nums[j]
                j-=1
        return res