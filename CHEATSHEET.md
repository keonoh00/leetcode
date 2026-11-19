# 알고리즘 Cheat Sheet

## 문제를 받으면

코드를 쓰기 전에 2분 동안 세 가지를 소리 내어 말한다.

1. **Constraints:** n이 얼마인가? 아래 표에서 시간 안에 도는 알고리즘을 고른다.
2. **Brute Force:** 가장 단순한 방법은 무엇이고, 무엇을 계속 반복하나? 그 반복을 없애는
   것이 쓸 기법이다. 기법마다 **왜 빠른가** 줄을 본다.
3. **단서:** 문제의 말이 어떤 기법을 가리키나? 기법마다 **단서** 줄을 본다.

알고리즘보다 규칙을 그대로 옮기는 게 일인 문제(Simulation)라면:

1. 반환값부터 읽는다: type, 순서, 맞는 게 없을 때 무엇을 반환하는지.
2. 규칙을 한 줄에 하나씩 주석으로 적는다. Tie-break("같으면…")와 예외("없으면…")도.
3. 데이터 모양을 정한다: 기록마다 tuple, id → 정보 dict, 정렬된 event list.
4. 규칙 하나에 함수 하나. `solution`은 parse, 반복, 함수 호출만 한다.
5. 첫 예제를 손으로 풀고, 중간 값을 `print`해서 맞춰 본다.

---

## n으로 고르기

파이썬은 1초에 간단한 연산을 약 10⁷번 한다. n²이 10¹⁰이면 통과하지 못한다.

왼쪽에서 내 n을 찾되, 올려서 찾는다: n ≤ 10⁴이면 10⁵ 줄을 본다. 표에서 더 아래에
있는 것은 더 빠르니 그것도 된다.

<table>
<tr><th>Constraint</th><th>Time</th><th>Algorithm</th></tr>
<tr><td>n ≤ 20</td><td>O(2ⁿ)</td><td>Backtracking: 모든 subset, 모든 순서</td></tr>
<tr><td rowspan="5">n ≤ 10³</td><td rowspan="4">O(n²)</td><td>Nested loop: 모든 쌍</td></tr>
<tr><td>Sort한 뒤 수마다 Two Pointers: 세 수의 합 (3Sum)</td></tr>
<tr><td>앞의 모든 j &lt; i를 보는 DP: LIS, Word Break</td></tr>
<tr><td>두 문자열 DP: LCS, Edit Distance</td></tr>
<tr><td>O(n × amount)</td><td>합마다 보는 DP: 합을 만드는 방법 수, 합이 target인 subset</td></tr>
<tr><td rowspan="17">n ≤ 10⁵</td><td rowspan="3">O(n log n)</td><td>먼저 Sort</td></tr>
<tr><td>Interval: start로 sort한 뒤 merge</td></tr>
<tr><td>Edge에 cost가 있는 Graph: Heap으로 Dijkstra</td></tr>
<tr><td>O(n log k)</td><td>크기 k인 Heap: 가장 큰, 작은, 가까운 k개</td></tr>
<tr><td>O(n log m)</td><td>답을 Binary Search: 조건을 만족하는 가장 작은 X (Koko)</td></tr>
<tr><td rowspan="10">O(n)</td><td>Hash Map, Set: 본 적 있나, 개수 세기, grouping</td></tr>
<tr><td>Prefix Sum + Hash Map: 합이 k인 subarray</td></tr>
<tr><td>Two Pointers: 정렬된 배열의 쌍, palindrome</td></tr>
<tr><td>Sliding Window: 가장 긴/짧은 substring, subarray</td></tr>
<tr><td>Stack: 다음으로 큰 값, 괄호 짝</td></tr>
<tr><td>for문 하나 DP: 방법의 수, 최고 합계</td></tr>
<tr><td>Linked List: dummy node, slow/fast pointer, in-place reverse</td></tr>
<tr><td>Binary Tree: DFS recursion, level별로는 BFS</td></tr>
<tr><td>Grid: 영역 세기는 DFS, 최소 이동은 BFS, 경로 수는 DP</td></tr>
<tr><td>Graph: adjacency list로 DFS나 BFS, 선수 과목은 Topological Sort</td></tr>
<tr><td>O(log n)</td><td>Binary Search: 정렬된 배열에서 값 찾기</td></tr>
<tr><td>호출마다 O(1)</td><td>Design: Hash Map + Linked List (LRU Cache), Min Stack</td></tr>
</table>

n은 입력의 길이다. Grid면 행 × 열, Graph면 node 수 + edge 수다. k는 문제에 나오는
k, m은 가장 큰 값이다. LIS는 Longest Increasing Subsequence, LCS는 Longest Common
Subsequence다.

---

## 기법별 정리

기법마다 단서, 방법, 왜 빠른가, 그리고 가장 쉬운 예시 문제 하나와 그 코드가 있다.

### Two Pointers
- **단서:** palindrome; 정렬된 배열에서 합이 target인 쌍이나 세 수
- **방법:** 양 끝에서 시작해 가운데로 좁혀 온다. 합을 찾을 때는 합이 작으면 left를
  오른쪽으로, 크면 right를 왼쪽으로 옮긴다.
- **왜 빠른가:** Brute Force는 모든 쌍을 본다, O(n²). 비교 한 번마다 한쪽 끝을
  버리니 O(n).
- **같은 기법:** Two Sum II, 3Sum, Container With Most Water

**예: Valid Palindrome (125, Easy).** 문자열 `s`에서 대문자는 소문자로 바꾸고 글자와
숫자가 아닌 문자는 지운다. 남은 문자열이 앞뒤로 읽어 같으면 `True`를 반환한다.
`"A man, a plan, a canal: Panama"` → `True` (`"amanaplanacanalpanama"`).

```python
def is_palindrome(s):
    chars = [ch.lower() for ch in s if ch.isalnum()]  # 글자와 숫자만, 소문자로
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1
    return True
```

시간 O(n), 공간 O(n). n = `len(s)`. 글자마다 한 번씩 본다.

### Hash Map, Set
- **단서:** "전에 본 적 있나?", 개수 세기, grouping
- **방법:** 본 것을 set이나 dict에 저장해 두고 찾는다
- **왜 빠른가:** list에서 찾으면 O(n)이지만 set과 dict는 O(1). 모든 쌍을 비교하는
  O(n²)이 O(n)이 된다.
- **같은 기법:** Two Sum, Group Anagrams, Top K Frequent Elements

**예: Contains Duplicate (217, Easy).** 정수 배열 `nums`에 같은 값이 두 번 이상
나오면 `True`, 모두 다르면 `False`. `[1, 2, 3, 1]` → `True`.

```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

시간 O(n), 공간 O(n). n = `len(nums)`.

### Prefix Sum + Hash Map
- **단서:** 합이 k인 subarray (연속된 부분 배열), 음수도 있음
- **방법:** i부터 j까지의 합 = (j까지의 prefix sum) - (i 앞까지의 prefix sum). 그래서
  지금의 `total`에서 `total - k`가 앞에 몇 번 나왔는지 Hash Map에서 찾는다.
- **왜 빠른가:** Brute Force는 모든 (i, j) 구간의 합을 구한다, O(n²). 구간 합을
  prefix sum의 차로 바로 알고, 필요한 값은 O(1)에 찾으니 O(n).
- **같은 기법:** Subarray Sum Equals K

**예: Subarray Sum Equals K (560, Medium).** 정수 배열 `nums`와 `k`가 주어진다.
합이 `k`인 subarray의 개수를 반환한다. `nums = [1, 1, 1], k = 2` → `2` (index 0–1과
1–2).

```python
def subarray_sum(nums, k):
    count = total = 0
    seen = {0: 1}  # prefix sum -> 지금까지 나온 횟수
    for num in nums:
        total += num
        count += seen.get(total - k, 0)  # 앞에 total - k가 있었으면, 그 뒤부터 여기까지 합이 k
        seen[total] = seen.get(total, 0) + 1
    return count
```

시간 O(n), 공간 O(n). n = `len(nums)`.

### Sliding Window
- **단서:** 연속된 substring이나 subarray: 길이가 k인 것, 또는 규칙을 지키는 가장
  긴/짧은 것
- **방법:** 구간을 한 칸 밀 때 새 값을 넣고 빠지는 값을 뺀다. 길이가 정해져 있지
  않으면 오른쪽을 늘리다가, 규칙이 깨지면 왼쪽을 줄인다.
- **왜 빠른가:** Brute Force는 구간마다 처음부터 다시 계산한다, O(n × k). 한 칸 밀
  때 바뀌는 것은 두 값뿐이니 O(n).
- **같은 기법:** Longest Substring Without Repeating Characters, Best Time to Buy
  and Sell Stock

**예: Maximum Average Subarray I (643, Easy).** 정수 배열 `nums`에서 길이가 정확히
`k`인 subarray의 평균 중 가장 큰 값을 반환한다. `nums = [1, 12, -5, -6, 50, 3], k = 4`
→ `12.75` (`[12, -5, -6, 50]`의 합 51 ÷ 4).

```python
def find_max_average(nums, k):
    total = sum(nums[:k])  # 첫 window
    best = total
    for right in range(k, len(nums)):
        total += nums[right] - nums[right - k]  # 새 수를 더하고, 빠지는 수를 뺀다
        best = max(best, total)
    return best / k
```

시간 O(n), 공간 O(1). n = `len(nums)`.

### Binary Search
- **단서:** 정렬된 입력, 또는 "조건을 만족하는 가장 작은 X" (X 하나를 확인하기는 쉬울
  때)
- **방법:** 가운데를 확인하고, 답이 있을 수 없는 절반을 버린다
- **왜 빠른가:** 하나씩 보면 O(n). 볼 때마다 절반을 버리니 O(log n). 10⁹개도 30번이면
  된다.
- **같은 기법:** Find Minimum in Rotated Sorted Array, Search a 2D Matrix, Koko
  Eating Bananas

**예 1: Binary Search (704, Easy).** 오름차순 정렬된 `nums`(값은 모두 다름)에서
`target`의 index를, 없으면 `-1`을 반환한다. `nums = [-1, 0, 3, 5, 9, 12], target = 9`
→ `4`.

```python
def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**예 2: First Bad Version (278, Easy).** 버전 `1`부터 `n`까지 중 어느 버전부터 불량이고,
그 뒤는 모두 불량이다. `is_bad_version(v)`(LeetCode에서는 `isBadVersion`)를 되도록 적게
불러 처음 불량인 버전을 찾는다. `n = 5`, 처음 불량이 4 → `4`.

```python
def first_bad_version(n):
    low, high = 1, n
    while low < high:
        mid = (low + high) // 2  # 내림
        if is_bad_version(mid):
            high = mid  # mid가 답일 수도 있으니 남긴다
        else:
            low = mid + 1
    return low
```

둘 다 시간 O(log n), 공간 O(1). 짝을 맞춘다: `high = mid - 1`은 `while low <= high`와
함께, `high = mid`는 `while low < high`와 내림과 함께 쓴다.

### Stack
- **단서:** 괄호 짝; 다음으로 큰 값
- **방법:** 아직 짝(답)을 기다리는 것을 쌓아 두고, 짝이 오면 pop한다
- **왜 빠른가:** 짝을 찾으려고 매번 앞을 다시 뒤지면 O(n²). 기다리는 것만 쌓아 두면
  짝은 항상 맨 위에 있으니 O(n).
- **같은 기법:** Daily Temperatures, Valid Parentheses

**예: Valid Parentheses (20, Easy).** `()[]{}`로만 된 문자열 `s`에서, 모든 여는 괄호가
같은 종류의 닫는 괄호로 올바른 순서로 닫히면 `True`. `"([])"` → `True`, `"([)]"` →
`False` (`[`가 닫히기 전에 `)`가 왔다).

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}  # 닫는 괄호 -> 여는 괄호
    stack = []  # 아직 짝을 기다리는 여는 괄호
    for ch in s:
        if ch not in pairs:
            stack.append(ch)  # 여는 괄호: push
        elif not stack or stack.pop() != pairs[ch]:
            return False  # 기다리는 괄호가 없거나, 짝이 틀렸다
    return not stack  # 짝을 못 찾은 여는 괄호가 없어야 한다
```

시간 O(n), 공간 O(n). n = `len(s)`.

### Heap
- **단서:** 가장 큰, 작은, 가까운 k개
- **방법:** 크기를 k로 유지하는 Heap. `heapq`는 Min Heap이라 맨 위가 가장 작은 값이다.
- **왜 빠른가:** 매번 정렬하면 O(n log n). Heap에 넣고 빼기는 O(log k).
- **같은 기법:** Kth Largest Element in an Array, K Closest Points to Origin, Last
  Stone Weight

**예: Kth Largest Element in a Stream (703, Easy).** `KthLargest(k, nums)` class를
만든다. `add(val)`마다 `val`을 넣고, 지금까지의 모든 수 중 k번째로 큰 수를 반환한다.
`k = 3, nums = [4, 5, 8, 2]`에서 `add(3)` → `4` (큰 순서로 8, 5, 4).

```python
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []  # 지금까지 가장 큰 k개
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)  # 가장 작은 것을 버린다
        return self.heap[0]  # 큰 k개 중 가장 작은 것 = k번째로 큰 수
```

`add` 한 번에 시간 O(log k), 공간 O(k).

### DFS, BFS
- **단서:** Grid의 영역, 퍼져 나가는 것, 최소 이동 횟수
- **방법:** 칸을 방문하면 표시하고, 이웃 칸을 방문한다. 최소 이동 횟수가 필요하면
  BFS(queue)를 쓴다.
- **왜 빠른가:** 방문 표시 덕에 칸마다 한 번만 본다, O(rows × cols). BFS는 가까운
  칸부터 보니, 목표에 처음 닿을 때가 최소 이동이다.
- **같은 기법:** Number of Islands, Max Area of Island, Rotting Oranges

**예 1, DFS: Flood Fill (733, Easy).** 2D grid `image`에서 시작 칸 `(sr, sc)`와
상하좌우로 이어진 같은 색 칸을 모두 `color`로 바꾼다. 그림판의 페인트 통과 같다.
`[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2` →
`[[2, 2, 2], [2, 2, 0], [2, 0, 1]]` (오른쪽 아래 `1`은 `0`에 막혀 그대로).

```python
def flood_fill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    old = image[sr][sc]
    if old == color:
        return image  # 이미 그 색: 칠해도 표시가 안 되니 끝없이 돈다

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != old:
            return
        image[r][c] = color  # 칠하는 것이 곧 방문 표시
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return image
```

**예 2, BFS: 미로 최단 거리 (예시 문제).** 문자열 list `grid`에서 `"."`은 길, `"#"`은
벽이다. `(0, 0)`에서 상하좌우로 움직여 오른쪽 아래 칸까지 가는 최소 이동 횟수를,
못 가면 `-1`을 반환한다. `["..#", "#..", "#.."]` → `4`.

```python
from collections import deque

def fewest_moves(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0)])
    seen = {(0, 0)}
    steps = 0
    while queue:
        for _ in range(len(queue)):  # 지금 거리에 있는 칸 전부
            r, c = queue.popleft()
            if (r, c) == (rows - 1, cols - 1):
                return steps
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue  # grid 밖
                if grid[nr][nc] == "#" or (nr, nc) in seen:
                    continue  # 벽이거나, 이미 넣은 칸
                seen.add((nr, nc))
                queue.append((nr, nc))
        steps += 1
    return -1
```

둘 다 시간 O(rows × cols), 공간 O(rows × cols).

### Dijkstra
- **단서:** edge에 cost가 있는 Graph의 최단 경로 (cost는 음수가 아님)
- **방법:** Heap에서 가장 가까운 node를 꺼내고, 그 node의 edge를 하나씩 시도한다
- **왜 맞는가:** 가장 가까운 node부터 꺼내면, 그 거리는 다른 길로 더 짧아질 수 없다.
  Cost가 모두 1이면 BFS로 충분하다.
- **같은 기법:** Network Delay Time

**예: Network Delay Time (743, Medium).** Node는 `1`부터 `n`까지이고, `times[i] =
[u, v, w]`는 `u`에서 `v`로 가는 데 `w`가 걸리는 한 방향 edge다. `k`에서 보낸 신호를
모든 node가 받는 시간을, 못 받는 node가 있으면 `-1`을 반환한다.
`times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2` → `2` (node 4가 2 → 3 → 4로
가장 늦다).

```python
import heapq
from collections import defaultdict
from math import inf

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, cost in times:
        graph[u].append((v, cost))  # 양방향이면 graph[v].append((u, cost))도 넣는다
    dist = {k: 0}
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # 더 짧은 길을 이미 찾은, 옛날 기록
        for v, cost in graph[u]:
            if d + cost < dist.get(v, inf):
                dist[v] = d + cost
                heapq.heappush(heap, (d + cost, v))
    return max(dist.values()) if len(dist) == n else -1
```

시간 O(E log E), 공간 O(n + E). E = edge 수(`len(times)`). Edge마다 Heap에 한 번 넣는다.

### Tree Recursion
- **단서:** Binary Tree
- **방법:** 왼쪽과 오른쪽 subtree의 답을 구해 합친다. Level별로 보려면 위의 BFS 틀을
  쓴다.
- **같은 기법:** Validate Binary Search Tree, Invert Binary Tree, Diameter of Binary
  Tree, Binary Tree Level Order Traversal

**예: Maximum Depth of Binary Tree (104, Easy).** Root에서 가장 먼 leaf까지 가는 경로의
node 수를 반환한다. 아래 tree(`[3, 9, 20, null, null, 15, 7]`) → `3` (3 → 20 → 15).

```text
    3
   / \
  9   20
     /  \
    15   7
```

```python
def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

시간 O(n), 공간 O(h). n = node 수, h = tree 높이 (recursion 깊이).

### Backtracking
- **단서:** 모든 subset이나 모든 순서, n ≤ 20
- **방법:** 하나를 고르고, recursion하고, 되돌린 뒤 다음 것을 고른다
- **왜 되는가:** n ≤ 20이면 2ⁿ ≈ 10⁶이라 전부 만들어 봐도 시간 안에 든다.
- **같은 기법:** Subsets, Permutations

**예: Subsets (78, Medium).** 값이 모두 다른 `nums`의 모든 subset(빈 집합 포함)을
반환한다. `[1, 2, 3]` → `[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]`.

```python
def subsets(nums):
    result = []
    path = []  # 지금까지 고른 수

    def backtrack(start):
        result.append(path[:])  # 지금 고른 것도 subset 하나 (복사해서 저장)
        for i in range(start, len(nums)):
            path.append(nums[i])  # 고른다
            backtrack(i + 1)  # 그 뒤의 수로 이어서 고른다
            path.pop()  # 되돌리고, 다음 수를 고른다

    backtrack(0)
    return result
```

시간 O(n × 2ⁿ): subset이 2ⁿ개이고 하나를 복사하는 데 최대 n.

### Sort, then Merge
- **단서:** 겹치는 interval
- **방법:** start로 sort한다. 다음 interval이 지금 interval이 끝나기 전에 시작하면
  merge한다.
- **왜 빠른가:** 정렬해 두면 겹칠 수 있는 것은 바로 앞 interval뿐이다. 모든 쌍을
  비교하는 O(n²)이 정렬 O(n log n)이 된다.
- **같은 기법:** Merge Intervals, Insert Interval, Non-overlapping Intervals

**예: Merge Intervals (56, Medium).** `[start, end]` list에서 겹치는 interval을 모두
합친다. 끝과 시작이 같아도 겹친다. `[[1, 3], [2, 6], [8, 10]]` → `[[1, 6], [8, 10]]`.

```python
def merge(intervals):
    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # 마지막 interval과 겹친다
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

시간 O(n log n), 공간 O(n). n = interval 수.

### Linked List
- **단서:** Linked List
- **방법:** Dummy node를 두면 head를 따로 처리하지 않아도 된다. Slow/fast pointer는
  fast가 2칸, slow가 1칸씩 간다.
- **같은 기법:** Reverse Linked List, Middle of the Linked List, Remove Nth Node From
  End of List

**예: Linked List Cycle (141, Easy).** `next`를 따라가다 이미 지난 node로 돌아오면
cycle이다. Cycle이 있으면 `True`. `3 → 2 → 0 → -4`이고 `-4`의 `next`가 `2` → `True`.

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:  # cycle 안에서 fast가 slow를 따라잡았다
            return True
    return False
```

시간 O(n), 공간 O(1). n = node 수.

### Dynamic Programming (DP)
- **단서:** 방법의 수; 가장 적은, 많은, 좋은 합계; "X를 만들 수 있나?"; 각 선택이
  앞의 선택에 달려 있다
- **방법:** 코드를 쓰기 전에 네 가지에 답한다.
  1. `dp[i]`는 무엇인가? "i번째 계단까지 오는 방법의 수"처럼 말로 한다.
  2. `dp[i]`를 더 작은 답으로 어떻게 만드나? 마지막 선택을 본다.
  3. Base case는 무엇인가? `dp[0]` 같은 것.
  4. 답은 어디 있나? `dp[n]`인가, `max(dp)`인가?
- **왜 빠른가:** 그냥 recursion은 같은 작은 문제를 계속 다시 푼다 (Climbing Stairs는
  O(2ⁿ)). 답을 표에 저장하면 작은 문제마다 한 번만 푼다 (O(n)).

| 유형 | 단서 | `dp[i]`의 뜻 | 만드는 재료 |
|---|---|---|---|
| 한 줄 | 계단, 한 줄로 선 집 | 앞의 i개에 대한 답 | `dp[i - 1]`과 `dp[i - 2]` |
| i에서 끝남 | LIS | 정확히 i에서 끝나는 것 중 최선 | j < i인 모든 `dp[j]` |
| 문자열 자르기 | s를 단어로 나눌 수 있나? | `s[:i]`를 나눌 수 있다 | `s[j:i]`가 단어인 `dp[j]` |
| 합 만들기 | 같은 수를 몇 번이든 써서 합 만들기 | 합 a를 만드는 방법 수 | 수마다 `dp[a - num]` |
| 한 번씩만 | 합이 target인 subset | 몇 개를 골라 합 s를 만들 수 있다 | `dp[s - num]`, s는 큰 쪽부터 |
| Grid | Grid의 경로 | 칸 (r, c)의 답 | 위 칸과 왼쪽 칸 |
| 두 문자열 | LCS, Edit Distance | `a[:i]`와 `b[:j]`의 답 | `dp[i - 1][j - 1]`, `dp[i - 1][j]`, `dp[i][j - 1]` |

**한 줄: Climbing Stairs (70, Easy).** 한 번에 1칸이나 2칸을 오를 때, `n`칸 계단을
오르는 방법의 수. `n = 3` → `3` (1+1+1, 1+2, 2+1).

```python
def climb_stairs(n):
    dp = [0] * (n + 1)  # dp[i] = i번째 계단까지 오는 방법 수
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 마지막에 1칸 올랐거나, 2칸 올랐거나
    return dp[n]
```

시간 O(n), 공간 O(n).

같은 문제를 top-down으로: 그냥 recursion을 쓰고 `@cache`를 붙이면 `i`마다 한 번만
계산한다. 파이썬은 recursion이 약 1,000번 깊어지면 멈추니, n이 크면 위의 표로 쓴다.

```python
from functools import cache

def climb_stairs(n):
    @cache
    def ways(i):  # i번째 계단까지 오는 방법 수
        if i <= 1:
            return 1
        return ways(i - 1) + ways(i - 2)

    return ways(n)
```

**한 줄, 변수 두 개로: House Robber (198, Medium).** 한 줄로 선 집의 돈 `nums`에서,
바로 옆 두 집은 함께 털 수 없을 때 털 수 있는 최댓값. `[2, 7, 9, 3, 1]` → `12`
(2 + 9 + 1).

```python
def rob(nums):
    prev2 = prev1 = 0  # 두 집 전까지의 최선, 한 집 전까지의 최선
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)  # 이 집을 건너뛰거나, 털거나
    return prev1
```

시간 O(n), 공간 O(1). `dp[i - 1]`과 `dp[i - 2]`만 쓰니 list가 필요 없다.

**i에서 끝남: Longest Increasing Subsequence (300, Medium).** 가장 긴 strictly
increasing subsequence(순서를 지키며 몇 개를 지운 것, 연속 아니어도 됨)의 길이.
`[10, 9, 2, 5, 3, 7, 101, 18]` → `4` (예: `[2, 3, 7, 101]`).

```python
def length_of_lis(nums):
    dp = [1] * len(nums)  # dp[i] = 정확히 i에서 끝나는 가장 긴 increasing subsequence
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:  # nums[i]를 nums[j] 뒤에 붙일 수 있다
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

시간 O(n²), 공간 O(n).

**문자열 자르기: Word Break (139, Medium).** `s`를 `word_dict`의 단어로만 빈틈없이
나눌 수 있으면 `True`. 같은 단어를 여러 번 써도 된다. `"applepenapple", ["apple",
"pen"]` → `True`.

```python
def word_break(s, word_dict):
    words = set(word_dict)
    dp = [True] + [False] * len(s)  # dp[i] = s[:i]를 단어로 나눌 수 있다
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:  # s[:j]는 나뉘고, s[j:i]는 단어다
                dp[i] = True
                break
    return dp[-1]
```

시간 O(n³): (j, i) 쌍이 n²개이고 `s[j:i]`를 자르는 데 최대 n. 공간 O(n).

**합 만들기: Combination Sum IV (377, Medium).** 서로 다른 양수 `nums`를 몇 번이든
골라 차례로 더해 `target`을 만드는 방법의 수 (순서가 다르면 다른 방법).
`[1, 2, 3], target = 4` → `7`. `nums = [1, 2]`이면 Climbing Stairs와 같다.

```python
def combination_sum4(nums, target):
    dp = [1] + [0] * target  # dp[a] = 합 a를 만드는 방법 수; 0은 아무것도 안 쓰는 1가지
    for a in range(1, target + 1):
        for num in nums:
            if num <= a:
                dp[a] += dp[a - num]  # 마지막에 쓴 수가 num
    return dp[target]
```

시간 O(target × len(nums)), 공간 O(target).

**한 번씩만: Partition Equal Subset Sum (416, Medium).** 양수 `nums`를 합이 같은 두
묶음으로 나눌 수 있으면 `True`. `[1, 5, 11, 5]` → `True` (`[1, 5, 5]`와 `[11]`). s를
큰 쪽부터 내려가야 `dp[s - num]`이 아직 이 수를 쓰기 전의 답이라, 같은 수를 두 번 쓰지
않는다.

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [True] + [False] * target  # dp[s] = 지금까지의 수 몇 개로 합 s를 만들 수 있다
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]  # num 없이, 또는 num을 써서
    return dp[target]
```

시간 O(n × target), 공간 O(target). n = `len(nums)`, target = 전체 합의 절반.

**Grid: Unique Paths (62, Medium).** `m × n` grid의 왼쪽 위에서 오른쪽이나 아래로만
움직여 오른쪽 아래까지 가는 경로의 수. `m = 3, n = 2` → `3`.

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]  # dp[r][c] = (r, c)까지 가는 경로 수; 맨 위 row와 맨 왼쪽 column은 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]  # 위에서 왔거나, 왼쪽에서 왔거나
    return dp[-1][-1]
```

시간 O(m × n), 공간 O(m × n).

**두 문자열: Longest Common Subsequence (1143, Medium).** 두 문자열 `a`, `b`(LeetCode의
`text1`, `text2`) 모두의 subsequence인 것 중 가장 긴 것의 길이. `"abcde", "ace"` → `3`.
Row 0과 column 0은 빈 문자열이라 0으로 둔다.

```python
def longest_common_subsequence(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]  # dp[i][j] = a[:i]와 b[:j]의 답
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # 마지막 글자가 같다: 둘 다 쓴다
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # a나 b에서 한 글자를 뺀다
    return dp[-1][-1]
```

시간 O(len(a) × len(b)), 공간도 같다.

---

## Python 도구

```python
# 시각: "HH:MM" -> 분, 그리고 다시 "HH:MM"
h, m = map(int, "09:05".split(":"))
minutes = h * 60 + m
f"{minutes // 60:02d}:{minutes % 60:02d}"      # 다시 "09:05"

# 날짜, 한 달이 모두 28일일 때
y, mo, d = map(int, "2026.11.22".split("."))
days = y * 12 * 28 + (mo - 1) * 28 + d

# 날짜, 실제 달력
from datetime import date, timedelta
(date(2026, 11, 22) - date(2026, 1, 1)).days   # 두 날짜 사이의 일수: 325
date(2026, 11, 22).weekday()                   # 월요일 = 0, 이날은 일요일이라 6
date(2026, 11, 22) + timedelta(days=30)        # 30일 뒤

# 개수 세기와 grouping
from collections import Counter, defaultdict
count = Counter("banana")                      # {"a": 3, "n": 2, "b": 1}; 없는 key는 0
total = defaultdict(int)                       # total[key] += x
groups = defaultdict(list)                     # groups[key].append(x)

# 정렬
sorted(rows, key=lambda r: (-r[1], r[0]))      # 점수 높은 순, 같으면 이름 A→Z
nums.sort()                                    # 제자리 정렬, None을 반환한다

# Max Heap: heapq는 Min Heap이라 음수로 넣고 꺼낼 때 다시 뒤집는다
import heapq
heapq.heappush(heap, -x)
largest = -heapq.heappop(heap)

# 올림 나눗셈, 양의 정수일 때
-(-a // b)                                     # a / b를 올림

# 모든 쌍, 순서, 조합
from itertools import combinations, permutations, product

# 정렬된 list에서 개수 세기
from bisect import bisect_left, bisect_right
bisect_right(a, x) - bisect_left(a, x)         # a에 x가 몇 개 있나
```

---

## 제출 전 체크

- **Edge case:** 빈 입력, 원소 하나, 모두 같은 값, 음수와 0, 가장 큰 입력.
- **답이 없을 때:** 문제가 정한 값(`-1`, `[]`, `False`)을 반환하나?
- **Index 범위:** `range(n)`은 n - 1까지, `s[i:j]`는 j 앞까지다.
- **2D list:** `[[0] * cols for _ in range(rows)]`로 만든다. `[[0] * cols] * rows`는
  모든 row가 같은 list라서 한 칸을 바꾸면 그 column 전체가 바뀐다.
- **Recursion 깊이:** 파이썬은 약 1,000번에서 멈춘다. 입력이 크면 BFS나 반복문으로 바꾼다.
