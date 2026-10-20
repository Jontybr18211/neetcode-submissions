class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = float('inf')
        low=0
        res = []
        for high in range(len(arr)):
            res.append(arr[high])
            while high-low+1>k:
                if abs(x-arr[low])>abs(x-arr[high]):
                    res.pop(0)
                else:
                    res.pop(-1)
                low+=1
        return res