class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        sourceSet = set()
        destinationSet = set()
        for i in range(len(paths)):
            src, dest = paths[i]
            sourceSet.add(src)
            destinationSet.add(dest)
        destinations = list(destinationSet)
        for dest in destinations:
            if dest not in sourceSet:
                return dest

            
        