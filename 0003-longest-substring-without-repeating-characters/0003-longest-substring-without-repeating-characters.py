class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        alpha_set = set()
        max_sequence = 0
        
        front_index = 0
        for char in s:
            
            while True:
                if char in alpha_set:
                    alpha_set.remove(s[front_index])
                    front_index += 1
                else:
                    break
            
            alpha_set.add(char)
            max_sequence = max(max_sequence, len(alpha_set))
        
        return max_sequence
                