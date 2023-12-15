import sys
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        arr = [0 for i in range(len(temperatures))]
        
        
        temp_date_map = {}
        
        for i in range(len(temperatures)-1, -1, -1):
            temp_date_map[temperatures[i]] = i
            
            min_increase_date = sys.maxsize
            for j in range(temperatures[i]+1, 101):
                if j in temp_date_map:
                    min_increase_date = min(min_increase_date, temp_date_map[j])
            
            if min_increase_date < sys.maxsize:
                arr[i] = min_increase_date - i
            
        return arr