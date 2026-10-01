class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        matching={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in matching:
                if not stack or stack[-1]!=matching[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack)==0