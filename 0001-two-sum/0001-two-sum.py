class Solution:
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        
        for i in range(len(nums)):
            
            # 이미 중복된 값이 있으면
            if nums[i] in dictionary:
                # 곱하기 2한 값을 타겟과 비교하여 조기종료
                if nums[i] * 2 == target:
                    return [i, dictionary[nums[i]]]
            else:
                dictionary[nums[i]] = i
        
        #반대 짝을 찾음
        for i in dictionary:
            pair = target - i
            
            if i != pair and pair in dictionary:
                return [dictionary[i], dictionary[pair]]
        