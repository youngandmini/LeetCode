class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictionary = {}
        
        # s에 각 문자가 몇개 들어있는지를 dict에 저장
        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        
        for char in t:
            if char in dictionary:
                dictionary[char] -= 1
            #t에 있는 문자가 s에 없으면 안됨
            else:
                return False
        
        # t의 문자 수보다 s의 문자 수가 더 많거나 적어도 안됨 
        for i in dictionary:
            if dictionary[i] != 0:
                return False
        
        return True
        