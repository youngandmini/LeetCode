class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def verify(t_dict):
            for key in t_dict:
                if t_dict[key] > 0:
                    return False
            return True
        
        
        t_dict = {}
        min_rear = -1
        min_front = -999999
        
        for char in t:
            t_dict[char] = t_dict.get(char, 0) +1
        
        front = 0
        rear = 0
        
        while True:
            if rear >= len(s):
                break
            
            if s[rear] in t_dict:
                t_dict[s[rear]] -= 1
                
                #0 이하가 되었다면 substring이 가능한지 확인
                if t_dict[s[rear]] <= 0:
                    
                    #substring이 가능하다면
                    if verify(t_dict):
                        while True:
                            
                            if front >= len(s) or front > rear:
                                break
                            
                            # print(front, rear, t_dict, s[front])
                            # t와 관련 없는 알파벳이라면 그냥 땡겨도 됨
                            if s[front] not in t_dict:
                                front += 1
                                continue
                            
                            # t와 관련 있는 알파벳이라면
                            else:
                                # 땡겨도 substring이 유지된다면 그냥 땡겨도 됨
                                if t_dict[s[front]] < 0:
                                    t_dict[s[front]] += 1
                                    front += 1
                                    continue
                                else:
                                    # 땡겼을 때 substring이 유지되지 않는다면 최소 길이를 업데이트 해줌
                                    if rear - front < min_rear - min_front:
                                        min_rear = rear
                                        min_front = front
                                    break
            #rear를 1 늘려줌
            rear += 1
        
        if min_rear == -1:
            return ""
        return s[min_front:min_rear+1]
            