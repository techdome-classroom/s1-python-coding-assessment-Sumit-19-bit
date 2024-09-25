def decode_message(s: str, p: str) -> bool:
    def match_helper(s_idx, p_idx):
        if s_idx == len(s) and p_idx == len(p):
            return True
        if p_idx == len(p):
            return False
        if s_idx == len(s):
            return p[p_idx] == '*' and match_helper(s_idx, p_idx + 1)

        if p[p_idx] == '?':
            return match_helper(s_idx + 1, p_idx + 1)
        
        if p[p_idx] == '*':
            return match_helper(s_idx, p_idx + 1) or match_helper(s_idx + 1, p_idx)
        
        if s[s_idx] == p[p_idx]:
            return match_helper(s_idx + 1, p_idx + 1)
        
        return False
    
    return match_helper(0, 0)