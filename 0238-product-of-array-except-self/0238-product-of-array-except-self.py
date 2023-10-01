class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1 for i in range(len(nums))]
        
        multi = 1
        # 현재 인덱스의 이전 값들에 대해서 곱함
        for i in range(len(nums)):
            result[i] *= multi
            multi *= nums[i]
        
        multi = 1
        # 위의 과정을 거꾸로 반복
        for i in range(len(nums)-1, -1, -1):
            result[i] *= multi
            multi *= nums[i]
            
        return(result)