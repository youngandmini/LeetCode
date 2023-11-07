class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha_dict = {}
        current_set = set()
        max_seq = 0
        front_index = 0

        for char in s:
            alpha_dict[char] = alpha_dict.get(char, 0) + 1
            current_set.add(char)

            loop_condition = True
            while loop_condition:
                max_alpha_len = 0
                total_len = 0
                if len(current_set) >= 2:
                    for current_char in current_set:
                        max_alpha_len  = max(max_alpha_len, alpha_dict[current_char])
                        total_len += alpha_dict[current_char]
                    if total_len - max_alpha_len <= k:
                        max_seq = max(max_seq, total_len)
                        loop_condition = False
                    else:
                        alpha_dict[s[front_index]] -= 1
                        if alpha_dict[s[front_index]] == 0:
                            current_set.remove(s[front_index])
                        front_index += 1
                else:
                    for current_char in current_set:
                        max_seq  = max(max_seq, alpha_dict[current_char])
                    loop_condition = False

        return max_seq
                