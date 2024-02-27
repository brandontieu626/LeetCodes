class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for t in tokens:
            if t in '+-*/':
                one=stack.pop()
                two=stack.pop()

                if t=='+':
                    stack.append(one+two)
                elif t=='-':
                    stack.append(two-one)
                elif t=='*':
                    stack.append(one*two)
                else:
                    stack.append(int(two/one))        
            else:
                stack.append(int(t))
        

        return stack.pop()