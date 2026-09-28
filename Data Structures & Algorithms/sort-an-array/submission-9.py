class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(arr,l,r):
            mid = (l + r) // 2
            arr[l], arr[mid] = arr[mid], arr[l]
            pivot = arr[l]
            i = l + 1
            j = r
            while True:
                while i<=j and arr[i]<=pivot:
                    i+=1
                while i<=j and arr[j]>pivot:
                    j-=1
                if i<=j:
                    arr[i],arr[j] = arr[j],arr[i]
                else:
                    break
            arr[l],arr[j] = arr[j],arr[l]
            return j
        
        def quickSort(arr,l,r):
            if l<r:
                pivot_index = partition(arr,l,r)
                quickSort(arr,l,pivot_index-1)
                quickSort(arr,pivot_index+1,r)
                  


        quickSort(nums,0,len(nums)-1)
        return nums