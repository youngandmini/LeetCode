class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)
        
        while True:
            index = (left+right)//2
            
            if nums[index] == target:
                return index
            if left+1 == right:
                break
            
            elif nums[index] < target:
                left = index
                continue
            
            elif nums[index] > target:
                right = index
                continue
        
        return -1