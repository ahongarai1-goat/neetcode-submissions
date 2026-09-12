class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
       
        from collections import Counter
        x=Counter(a)
        y=Counter(b)
        if dict(x)==dict(y):
            return True
        else:
            return False


        