# Find if Path Exists in Graph — Easy (#1971)
# https://leetcode.com/problems/find-if-path-exists-in-graph/

r"""
There is an undirected graph with n vertices, labelled 0 to n - 1. The edges are
given as a list, where edges[i] = [u_i, v_i] connects u_i and v_i both ways. No two
edges are the same, and no edge connects a vertex to itself.

Return true if there is a path from vertex source to vertex destination, and false
otherwise.

Example 1:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    Explanation: 0 -> 2 directly, or 0 -> 1 -> 2.

Example 2:
    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0,
    destination = 5
    Output: false
    Explanation: 0, 1 and 2 are connected to each other, and 3, 4 and 5 are
    connected to each other, but there is no edge between the two groups.

Constraints:
  - 1 <= n <= 2 * 10^5
  - 0 <= edges.length <= 2 * 10^5
  - edges[i].length == 2
  - 0 <= u_i, v_i <= n - 1
  - u_i != v_i
  - 0 <= source, destination <= n - 1
  - There are no duplicate edges."""


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        q = deque()
        q.append(source)
        seen = {source}
        while q:
            sou = q.pop()
            if sou == destination:
                return True
            des = graph[sou]

            for d in des:
                if d in seen:
                    continue
                seen.add(d)
                q.append(d)

        return False


CASES = [
    ((3, [[0, 1], [1, 2], [2, 0]], 0, 2), True),
    ((6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False),
]

if __name__ == "__main__":
    from leetcode import run

    run(Solution().validPath, CASES)
