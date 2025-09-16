        
#Use a stack to keep track of opening brackets
#When a closing bracket is encountered, check if it matches the top of the stack
#If it matches, pop the top of the stack
#If it doesn't match or the stack is empty, return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['{','(','[']:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                t=stack.pop(-1)
                if t=='[' and i==']':
                    pass
                elif t=='(' and i==')':
                    pass
                elif t=='{' and i=='}':
                    pass
                else:
                    return False
        if len(stack)!=0:
            return False
        return True