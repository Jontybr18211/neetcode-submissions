class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev_arr(arr,start,end):
            
            while end>start:
                arr[start],arr[end]=arr[end],arr[start]
                start,end=start+1,end-1

        k = k % len(nums)
        rev_arr(nums,0,len(nums)-1)
        rev_arr(nums,0,k-1)
        rev_arr(nums,k,len(nums)-1)       
        return nums