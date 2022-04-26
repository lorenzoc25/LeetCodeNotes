# 1584. Min Cost to Connect All Points | [Link](https://leetcode.com/problems/min-cost-to-connect-all-points/)

## Idea
To use Prim's algorithm: construct a MST iteratively by always choosing the edge that is the closest to the existing MST. In the optimize version, we will update the closet point to the MST every time we choose to add a point to the MST. The overall runtime is $O(n^2)$

## Code
```py
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost = 0
        edges_used = 0
        
        get_dist = lambda p1,p2: abs(points[p1][0] - points[p2][0]) + \
                                 abs(points[p1][1] - points[p2][1])
        
        included = [0] * n
        min_cost = [float('inf')] * n
        min_cost[0] = 0 # doesn't have to be 0, can be any random point to start with
        
        while edges_used < n:
            curr_min_edge = float('inf')
            chosen_node = -1
            # find one node that is closest to the existing MST
            for node in range(n):
                if not included[node] and min_cost[node] < curr_min_edge:
                    curr_min_edge = min_cost[node]
                    chosen_node = node
            
            # add the chosen node to MST
            cost += curr_min_edge
            included[chosen_node] = 1
            edges_used += 1
            
            # update the new min_cost from the existing MST
            for next_node in range(n):
                new_dist = get_dist(chosen_node, next_node)
                # if smaller, udpate it
                if not included[next_node] and new_dist < min_cost[next_node] :
                    min_cost[next_node] = new_dist

        return cost
```