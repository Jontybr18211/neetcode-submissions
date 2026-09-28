class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quick
        def partition(arr,l,r):
            mid = (l+r)//2
            arr[mid],arr[l]=arr[l],arr[mid]
            pivot = arr[l]
            i=l
            j=r
            while True:
                while i<=j and arr[i]<=pivot:
                    i+=1
                while i<=j and arr[j]>pivot:
                    j-=1
                if i<=j:
                    arr[i],arr[j]=arr[j],arr[i] 
                else:
                    break
            arr[l],arr[j]=arr[j],arr[l]
            return j
        def quickSort(arr,l,r):
            if l<r:
                partition_index = partition(arr,l,r)
                quickSort(arr,l,partition_index-1)
                quickSort(arr,partition_index+1,r)

        quickSort(nums,0,len(nums)-1)
        return nums