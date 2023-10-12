class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        front_index = 0
        rear_index = len(numbers)-1
        
        while True:
            
            if numbers[front_index] + numbers[rear_index] == target:
                return [front_index+1, rear_index+1]
            
            if numbers[front_index] + numbers[rear_index] < target:
                front_index += 1
            else:
                rear_index -= 1