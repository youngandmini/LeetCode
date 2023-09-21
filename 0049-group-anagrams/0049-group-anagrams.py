class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            
        index = 0
        result = []
        
        #해당 애너그램이 들어가있는 위치에 대한 매핑정보
        dictionary = {}
        
        #각각의 문자에 대해
        for string in strs:
            
            #정렬해서
            sorted_str = "".join(sorted(string))
            
            #dictionary에 정렬한 값이 있다면
            if sorted_str in dictionary:
                #동일한 애너그램 위치에 append
                result[dictionary[sorted_str]].append(string)
            else:
                #없으면 새로 추가
                result.append([string])
                dictionary[sorted_str] = index
                index += 1
        
        return result