class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif stack[-1] == s[i]:
                stack.pop()
            elif stack[-1] != s[i]:
                stack.append(s[i])
        #     print("stack at each level is ",stack)
        # print("stack is ",stack,"".join(stack))
        return "".join(stack)
