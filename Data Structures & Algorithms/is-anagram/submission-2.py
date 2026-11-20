class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_map={}
        t_map={}
        for c in s:
            if c in c_map:
                c_map[c] += 1
            else:
                c_map[c] = 1
        for r in t:
            if r in t_map:
                t_map[r] += 1
            else:
                t_map[r] = 1
        return c_map==t_map
            
