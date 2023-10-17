class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #일단 투포인터로 풀긴 했는데, 이게 과연 맞을까?
        #둘중 더 작은놈을 땡기는 것
        n = len(height)
        
        front_index = 0
        rear_index = n-1
        
        max_water = 0
        while True:
            if front_index >= rear_index:
                break
            
            water = (rear_index-front_index) * min(height[rear_index], height[front_index])
            max_water = max(max_water, water)
            
            if height[front_index] > height[rear_index]:
                rear_index -= 1
                continue
            elif height[front_index] < height[rear_index]:
                front_index += 1
                continue
            else:
                rear_index -= 1
                front_index += 1
        return max_water