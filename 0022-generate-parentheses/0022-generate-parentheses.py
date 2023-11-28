class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def recur(now, open_braket, close_braket):
            nonlocal result
            
            if open_braket == n and close_braket == n:
                result.append(now)
                return
            
            if open_braket <= close_braket:
                recur(now+"(", open_braket+1, close_braket)
            
            elif open_braket == n:
                recur(now+")", open_braket, close_braket+1)
            else:
                recur(now+")", open_braket, close_braket+1)
                recur(now+"(", open_braket+1, close_braket)
        
        result = []
        recur("", 0, 0)
        
        return result