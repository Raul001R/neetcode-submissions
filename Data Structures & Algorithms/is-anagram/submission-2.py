class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counters = {}
        countert = {}

        for i in s:
            counters[i] = 1 + counters.get(i,0)
        for i in t:
            countert[i] = 1 + countert.get(i,0)

        return counters == countert

    