class Solution:
    def trap(self, height: List[int]) -> int:
        
        def calc_water(start, end, height):
            water_height = min(height[start], height[end])
            water_amount = 0
            for i in range(start + 1, end):
                water_amount += water_height - height[i]

            return water_amount

        from_index = 0
        to_index = len(height) - 1
        result = 0

        while True:
            if from_index >= to_index:
                break

            for i in range(from_index+1, to_index + 1):
                if height[from_index] <= height[i]:
                    result += calc_water(from_index, i, height)
                    from_index = i

            if from_index >= to_index:
                break

            for j in range(to_index, from_index - 1, -1):
                if height[to_index] <= height[j]:
                    result += calc_water(j, to_index, height)
                    to_index = j

        return result