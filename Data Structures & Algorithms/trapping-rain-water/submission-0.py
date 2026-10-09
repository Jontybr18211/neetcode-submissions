class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n=len(heights)
        leftMax,rightMax = [0]*n,[0]*n
        leftMax[0]=heights[0]
        rightMax[n-1]=heights[n-1]
        for i in range(1,len(leftMax)):
            leftMax[i] = max(leftMax[i-1],heights[i])
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],heights[i])
        res = 0
        for i in range(len(heights)):
            res += min(leftMax[i],rightMax[i]) - heights[i]
        return res