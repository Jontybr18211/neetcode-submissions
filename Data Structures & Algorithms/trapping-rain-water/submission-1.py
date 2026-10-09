class Solution:
    def trap(self, height: List[int]) -> int:
        res = left = 0
        right=len(height)-1
        leftMax=height[left]
        rightMax=height[right]
        while right>left:
            if leftMax<rightMax:
                left+=1
                leftMax = max(leftMax,height[left])
                res += leftMax - height[left]
            else:
                right-=1
                rightMax = max(rightMax,height[right])
                res += rightMax - height[right]
        return res