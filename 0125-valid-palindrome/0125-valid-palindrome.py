class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        alphanumeric = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}
        
        s = s.lower()
        
        front_index = 0
        rear_index = len(s)-1
        
        while front_index < rear_index:
            
            if s[front_index] not in alphanumeric:
                front_index += 1
                continue
                
            if s[rear_index] not in alphanumeric:
                rear_index -= 1
                continue
            
            if s[front_index] != s[rear_index]:
                return False
            
            front_index += 1
            rear_index -= 1
        
        
        return True