class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        actualVowels = ['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in actualVowels:
                vowels.append(i)
        t = []
        vowels.sort()
        k = 0
        print("Sorted vowels are ",vowels)
        for i in range(len(s)):
            if s[i] not in actualVowels:
                t.append(s[i])
            else:
                t.append(vowels[k])
                k += 1
        print("Final t is ",t,"".join(t))
        return "".join(t)


            
        