class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in dict:
                dict[sorted_string].append(s)
            else:
                dict[sorted_string] = [s]
        return list(dict.values())
