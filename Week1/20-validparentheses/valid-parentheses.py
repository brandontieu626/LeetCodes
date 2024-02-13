class Solution:
    def isValid(self, s: str) -> bool:
        Lstack=[]

        for c in s:
            if c==']' or c==')' or c=='}':
                if Lstack:
                    top=Lstack.pop()
                    
                    if c==']':
                        if top!='[':
                            return False
                    elif c==')':
                        if top!='(':
                            return False
                    else:
                        if top!='{':
                            return False
                else:
                    return False
            else:
                Lstack.append(c)
        

        if len(Lstack)==0:
            return True
        
        return False
