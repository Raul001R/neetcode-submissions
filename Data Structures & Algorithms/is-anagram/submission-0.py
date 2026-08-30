class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        counter_s = {}
        counter_t = {}

        for i in s:
            counter_s[i] = 1 + counter_s.get(i,0) 

        for i in t:
            counter_t[i] = 1 + counter_t.get(i,0)

        return counter_s == counter_t 