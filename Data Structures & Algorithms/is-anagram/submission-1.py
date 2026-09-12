class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        b=list(t)
        x={}
        y={}
        for i in a:
            if i in x:
                x[i]+=1
            else:
                x[i]=1
        for j in b:
            if j in y:
                y[j]+=1
            else:
                y[j]=1
        if x==y:
            return True
        else:
            return False
        
            
        
        

        