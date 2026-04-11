# equations is an array of variable pairs, values is an array of real numbers
# equations[i] being [A, B] and values[i] being X represents the equation A / B = X
# queries is an array of variable pairs
# queries[j] being [C, D] represents the jth query where you must find the answer for C / D
# as the jth element of the array you return
# if you can't find C / D, return -1.0
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph with all the variables as nodes
        graph = defaultdict(defaultdict)

        # backtracking iterates over solutions in the search space
        # while the constraint is not met
        # in this case, the constraint is ret being -1.0
        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            # you start by visiting this node
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]

            # you can immediately find the target node
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    # don't re-visit neighbors
                    if neighbor in visited:
                        continue
                    # visit unvisited neighbors
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    # when you find a match, take it
                    if ret != -1.0:
                        break
            
            # you're done trying to find thing from this node
            visited.remove(curr_node)
            return ret

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results
        
