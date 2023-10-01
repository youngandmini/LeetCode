class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_map = {}
        
        for num in nums:
            num_map[num] = True
        
        lcs = 0
        for key in num_map:
            if num_map[key] == False:
                continue
            
            num_map[key] = False
            cs = 1
            less = key - 1
            greater = key + 1
            while True:
                if less in num_map:
                    num_map[less] = False
                    cs += 1
                    less -= 1
                else:
                    break
            while True:
                if greater in num_map:
                    num_map[greater] = False
                    cs += 1
                    greater += 1
                else:
                    break
            
            if lcs < cs:
                lcs = cs
            
        return lcs