class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        columns = [row[k] for row in score]
        score = sorted(score, key = lambda x :x[k], reverse = True)
        return score


        