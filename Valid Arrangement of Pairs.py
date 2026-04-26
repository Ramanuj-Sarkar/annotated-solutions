'''
Pairs is a 0-indexed 2D integer array consisting of lists like [start, end].

An arrangement of pairs is valid if
for every i where 1 <= i < pairs.length
we have pairs[i-1][1] == pairs[i][0].

Return any valid arrangement of pairs.

Assume there exists a valid arrangement of pairs.
'''
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # graph represents adjacency list, inOutDeg tracks in/out degree difference
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        # Build graph and count in/out degrees
        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1  # out-degree
            inOutDeg[end] -= 1    # in-degree

        # Find starting node 
        startNode = pairs[0][0] 
        for node in inOutDeg:
            # this is the correct start node in this case
            # because it has an out-degree and no in-degree
            if inOutDeg[node] == 1:
                startNode = node
                break

        # will get answer backwards
        path = []

        # do depth-first search
        def dfs(curr):
            while graph[curr]:
                nextNode = graph[curr].pop()
                dfs(nextNode)
                path.append((curr, nextNode))

        dfs(startNode)

        return path[::-1]
