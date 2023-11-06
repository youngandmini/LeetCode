class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_dict = {}
        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1
        
        
        for i in range(len(s2)-len(s1)+1):
            target = s2[i:i+len(s1)]
            s2_dict = {}
            for char in target:
                s2_dict[char] = s2_dict.get(char, 0) + 1
            if s1_dict == s2_dict:
                return True
        
        return False