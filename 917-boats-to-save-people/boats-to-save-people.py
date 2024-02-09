class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low = 0
        high = len(people) - 1
        count = 0
        while low <= high:
            if people[low] + people[high] <= limit:
                low += 1
                high -= 1
            else:
                high -= 1
            count += 1
        return count