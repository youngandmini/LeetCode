class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         #num - num의 개수에 대한 매핑정보
#         num_count_map = {}
#         #개수가 count인 num들의 리스트
#         count_num_map = {}
        
#         def remove_from_count_num_map(num, count):
#             count_num_map[count].remove(num)
        
#         def append_to_count_num_map(num, count):
#             if count in count_num_map:
#                 count_num_map[count].append(num)
#             else:
#                 count_num_map[count] = [num]


#         for num in nums:
#             if num in num_count_map:
#                 remove_from_count_num_map(num, num_count_map[num])
#                 num_count_map[num] += 1
#                 append_to_count_num_map(num, num_count_map[num])
#             else:
#                 num_count_map[num] = 1
#                 append_to_count_num_map(num, 1)

        
#         count = max(count_num_map.keys())
#         result = []
        
#         while k > 0:
            
#             for num in count_num_map[count]:
#                 k -= 1
#                 result.append(num)
#             count -= 1
        
#         return result

        #num - num의 개수에 대한 매핑정보
        num_count_map = {}
        #개수가 count인 num들의 집합
        count_num_map = {}
        
        def remove_from_count_num_map(num, count):
            count_num_map[count].remove(num)
        
        def append_to_count_num_map(num, count):
            if count in count_num_map:
                count_num_map[count].add(num)
            else:
                count_num_map[count] = {num}


        for num in nums:
            if num in num_count_map:
                remove_from_count_num_map(num, num_count_map[num])
                num_count_map[num] += 1
                append_to_count_num_map(num, num_count_map[num])
            else:
                num_count_map[num] = 1
                append_to_count_num_map(num, 1)

        
        count = max(count_num_map.keys())
        result = []
        
        while k > 0:
            
            for num in count_num_map[count]:
                k -= 1
                result.append(num)
            count -= 1
        
        return result
            