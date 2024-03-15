class Solution:
    def myAtoi(self, s: str) -> int:
        length=len(s)
        i=0
        negative=False
        if length==0:
          return 0
        while i<length and s[i]==" ":
            i+=1
        
        if i==length:
            return 0
        
        if s[i]=="-":
            negative=True
            i+=1
        elif s[i]=="+":
            i+=1
          
        
        total=0
        while i<length and s[i]=="0":
            i+=1

        while i<length and s[i] in "0123456789":
            total*=10
            total+=ord(s[i])-ord('0')
            i+=1
        
        if negative:
            total*=-1
        
        if total<(-2**31):
            total=-2**31
        elif total>(2**31-1):
            total=2**31-1
        
        return total