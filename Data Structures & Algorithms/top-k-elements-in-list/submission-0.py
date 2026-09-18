class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        sorted_elements = sorted(freq, key=freq.get)
        return sorted_elements[-k:]