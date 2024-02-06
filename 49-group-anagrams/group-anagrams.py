class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalList = defaultdict(list)
        for word in strs:
            sortedWord = "".join(sorted(word))
            finalList[sortedWord].append(word)
        res = list(finalList.values())
        return res