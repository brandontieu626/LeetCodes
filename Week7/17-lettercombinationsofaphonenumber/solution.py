class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetter={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]

        def combination(i,temp):
            if i>=len(digits):
                res.append(temp[:])
                return 
            
            letters=numToLetter[digits[i]]

            for c in letters:
                combination(i+1,temp+c)
        
        if digits:
            combination(0,"")
        
        return res