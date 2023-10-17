class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        fixed_number_set = set()
        n = len(nums)
        result = []
        for i in range(n-2):
            if nums[i] in fixed_number_set:
                continue
            
            fixed_number_set.add(nums[i])
            
            front_index = i+1
            rear_index = n-1
            target_sum = -nums[i]
            
            while front_index < rear_index:
                
                if nums[front_index] + nums[rear_index] > target_sum:
                    rear_index -= 1
                    continue
                elif nums[front_index] + nums[rear_index] < target_sum:
                    front_index += 1
                    continue
                
                #같다면
                result.append([nums[i], nums[front_index], nums[rear_index]])
                if nums[front_index] == nums[rear_index]:
                    break
                
                #이후에 또 똑같은 경우를 반복하지 않기 위해 달라질때까지 땡겨줌
                front_index+=1
                while nums[front_index] == nums[front_index-1]:
                    front_index+=1
                    
                rear_index-=1
                while nums[rear_index] == nums[rear_index+1]:
                    rear_index-=1
                continue
        return result
            