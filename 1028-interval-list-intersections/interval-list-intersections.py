class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        res = []
        for i in range(len(firstList)):
            first_start = firstList[i][0]
            first_end = firstList[i][1]
            for j in range(len(secondList)):
                sec_start = secondList[j][0]
                sec_end = secondList[j][1]
                
                # if first_end < sec_start:
                #     print('first_end and sec_start ',first_end, sec_start)
                #     break
                # print('sec_start ', sec_start, first_end,sec_end)

                    # break
                if sec_start <= first_start and sec_end >= first_start:
                    res.append([first_start, min(first_end, sec_end)])
                if first_end >= sec_start:
                    if first_start == sec_end:
                        if [first_start, first_start] not in res:
                            res.append([first_start, first_start])
                        # print('in if, I added ',first_start, first_start)
                    elif first_start < sec_start:
                        common_end = min(first_end, sec_end)
                        if([sec_start, common_end] not in res):
                            res.append([sec_start, common_end])
                        # print('in elsse, I added ',sec_start, common_end)
                    # break
                
        print('res is ',res)
        return res

