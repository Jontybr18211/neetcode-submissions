class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr,l,r,m):
            left,right = arr[l:m+1],arr[m+1:r+1]
            i,j,k = 0,0,l
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                k+=1
            while i<len(left):
                arr[k]=left[i]
                k+=1
                i+=1
            while j<len(right):
                arr[k]=right[j]
                k+=1
                j+=1

        def mergeSort(arr,l,r):
            if l<r:
                m = (l+r)//2
                mergeSort(arr,l,m)
                mergeSort(arr,m+1,r)
                merge(arr,l,r,m)
            return arr

        return mergeSort(nums,0,len(nums)-1)