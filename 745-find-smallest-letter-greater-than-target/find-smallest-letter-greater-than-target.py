class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mini  = 'z'
        found = 0
        for i in letters:
            if ord(i)>ord(target) and ord(mini)>= ord(i):
                mini = i
                found = 1
        if found == 0:
            return letters[0]
        return mini