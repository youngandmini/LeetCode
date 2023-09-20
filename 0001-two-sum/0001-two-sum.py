class Solution:
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        
        for i in range(len(nums)):
            
            pair = target - nums[i]
            #이미 짝이 있다면 반환
            if pair in dictionary:
                return [i, dictionary[pair]]
            
            else:
                dictionary[nums[i]] = i
        