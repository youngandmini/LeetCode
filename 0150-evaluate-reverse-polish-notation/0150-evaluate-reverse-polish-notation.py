class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for token in tokens:
            
            if token == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 + n1)
            elif token == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif token == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 * n1)
            elif token == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                sub_result = n2 // n1
                if n2 // n1 < 0 and n2 % n1 != 0:
                    sub_result+=1
                stack.append(sub_result)
            else:
                stack.append(int(token))
        return(stack.pop())