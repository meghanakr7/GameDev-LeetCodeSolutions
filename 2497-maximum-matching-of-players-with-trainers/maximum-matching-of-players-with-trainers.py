class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        ind = 0
        for i in range(len(players)):
            for j in range(ind, len(trainers)):
                if(players[i] <= trainers[j]):
                    count += 1
                    ind = j + 1
                    break
        return count