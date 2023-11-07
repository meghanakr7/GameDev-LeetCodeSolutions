class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        canVisit = []
        visited = set()
        for i in range(len(rooms[0])):
            if rooms[0][i] not in visited:
                canVisit.append(rooms[0][i])
                visited.add(rooms[0][i])
        visited.add(0)
        while canVisit:
            room = canVisit.pop()
            for i in range(len(rooms[room])):
                if rooms[room][i] not in visited:
                    canVisit.append(rooms[room][i])
                    visited.add(rooms[room][i])
            print("CanVisit is ",canVisit)
        print("visited is ",visited)
        if len(visited) == len(rooms):
            return True
        return False

        